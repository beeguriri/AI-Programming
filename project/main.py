import numpy as np
import csv

# hyper parameter
RND_MEAN = 0
RND_STD = 0.003
LEARNING_RATE = 0.0001

# csv -> numpy 배열로 변경
def load_dataset():
    global data, input_cnt, output_cnt
    # 파일 읽기
    with open('data/abalone.csv') as csv_file:
        # 자료 구조 : list
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)  # csv file header 제외 하기 =f.readline()
        rows = []
        for row in csv_reader:
            rows.append(row)

    input_cnt, output_cnt = 10, 1  # pandas => pd.read_csv(fileName, header=None, names=[column names])
    data = np.zeros([len(rows), input_cnt + output_cnt])

    # enumerate : 인덱스 번호와 컬렉션의 원소를 튜플 형태로 반환
    # zip : 동일한 개수로 이루어진 자료형을 묶어서 튜플의 형태로 반환
    for n, row in enumerate(rows):
        # 원-핫 인코딩
        if row[0] == "I":
            data[n, 0] = 1
        if row[0] == "M":
            data[n, 1] = 1
        if row[0] == "F":
            data[n, 2] = 1
        data[n, 3:] = row[1:]


# 결과물 : 기울기와 절편
# 기준값, weight 필요함
def init_model():
    global weight, bias, input_cnt, output_cnt
    weight = np.random.normal(RND_MEAN, RND_STD, [input_cnt, output_cnt]) # numpy는 뒤에서부터 읽는다! 1열 10행!
    bias = np.zeros([output_cnt])


def train_and_test(epoch_count=10, mb_size=10):
    # 1. 데이터 나누기(8:2), 배치 사이즈 결정 (local search size)
    step_count = arrange_data(mb_size)
    test_x, test_y = get_data_test()

    # 2. 학습 (=> 행렬 곱) : 오차(손실)와 정확도
    # epoch size, mb_size, step_count
    for epoch in range(epoch_count):
        losses = []
        accs = []
        for n in range(step_count):
            acc = run_test(test_x, test_y)
            train_x, train_y = get_train_data(mb_size, n)
            loss, acc = run_train(train_x, train_y) # 순전파
            losses.append(loss)
            accs.append(acc)

        print(f"Epoch {epoch+1} : loss={np.mean(losses):5.3f}, accs={np.mean(accs):5.3f}, accs={np.mean(acc):5.3f}")

    # 3. 테스트
    final_acc = run_test(test_x, test_y)
    print(f"Accs={np.mean(final_acc):5.3f}")

def run_train(x, y):
    # 순방향 => 정확도
    output, aux_nn = forward_neuralnet(x)
    loss, aux_pp = forward_postproc(output, y)
    accuracy = eval_accuracy(output, y)

    # 역방향 => 손실(오차)
    G_loss = 1.0
    G_output = backprop_postproc(G_loss, aux_pp)
    backprop_neuralnet(G_output, aux_nn)  # 기울기와 절편 수정

    return loss, accuracy


def run_test(x, y):
    output, aux_nn = forward_neuralnet(x)
    accuracy = eval_accuracy(output, y)

    return accuracy


def forward_neuralnet(x):
    # y = w1*x1 + b
    global weight, bias
    output = np.matmul(x, weight) + bias

    return output, x


def forward_postproc(output, y):
    diff = output - y
    square = np.square(diff)
    loss = np.mean(square)

    return loss, diff


def eval_accuracy(output, y):
    mdiff = np.mean(np.abs((output-y)/y))

    return 1 - mdiff


def backprop_postproc(G_loss, diff):

    # 오차의 기울기 구하기
    shape = diff.shape
    g_loss_square = np.ones(shape) / np.prod(shape)
    g_square_diff = 2 * diff
    g_diff_output = 1

    G_square = g_loss_square * G_loss
    G_diff = g_square_diff * G_square
    G_output = g_diff_output * G_diff

    return G_output


def backprop_neuralnet(G_output, aux_nn):

    # 역전파 편미분
    global weight, bias
    g_output_w = aux_nn.transpose()

    G_w = np.matmul(g_output_w, G_output)
    G_b = np.sum(G_output, axis=0)

    weight -= LEARNING_RATE * G_w
    bias -= LEARNING_RATE * G_b


def arrange_data(mb_size):
    global data, shuffle_map, test_begin_idx
    shuffle_map = np.arange(data.shape[0])  # -> NDArray
    np.random.shuffle(shuffle_map)
    step_count = int(data.shape[0] * 0.8) // mb_size
    test_begin_idx = step_count * mb_size

    return step_count  # mb_size 의존


def get_data_test():
    global data, shuffle_map, test_begin_idx, output_cnt
    test_data = data[shuffle_map[test_begin_idx:]]

    return test_data[:, :-output_cnt], test_data[:, -output_cnt:]


def get_train_data(mb_size, nth):
    global data, shuffle_map, test_begin_idx, output_cnt
    if nth == 0:
        np.random.shuffle(shuffle_map[:test_begin_idx])

    train_data = data[shuffle_map[mb_size*nth : mb_size*(nth+1)]]

    return train_data[:, :-output_cnt], train_data[:, -output_cnt:]


if __name__ == "__main__":
    # 입력
    load_dataset()  # CSV 파일 읽기
    # 처리
    init_model()  # 기울기와 절편 배열 data[x,y]
    # 출력
    train_and_test()  # epoch, batch_size
