
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

class Model:
    def __init__(self, file_path):
        self.file_path = file_path

    def run(self):
        # Загрузка данных из файла
        data = pd.read_excel(self.file_path, header=None, names=['value'])

          # Подготовка данных
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(data['value'].values.reshape(-1, 1))

        # Определение размера тестового набора в процентах
        test_size_percentage = 0.25  # Пример: 5%

        training_data_len = int(np.ceil(len(scaled_data) * (1 - test_size_percentage)))

        train_data = scaled_data[0:training_data_len, :]

        # Определение размера окна для обучения
        window_size = 60 if len(train_data) >= 60 else len(train_data) - 1

        # Создание датасета для обучения
        x_train, y_train = [], []

        for i in range(window_size, len(train_data)):
            x_train.append(train_data[i - window_size:i, 0])
            y_train.append(train_data[i, 0])

        x_train, y_train = np.array(x_train), np.array(y_train)

        # Изменение формы данных для LSTM
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

        # Создание модели LSTM
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
        model.add(LSTM(units=50, return_sequences=False))
        model.add(Dense(units=25))
        model.add(Dense(units=1))

        # Компиляция модели
        model.compile(optimizer='adam', loss='mean_squared_error')

        # Обучение модели
        model.fit(x_train, y_train, batch_size=1, epochs=1)

        # Создание тестового набора данных
        test_data = scaled_data[training_data_len - window_size:, :]

        x_test = []
        y_test = data['value'][training_data_len:].values

        for i in range(window_size, len(test_data)):
            x_test.append(test_data[i - window_size:i, 0])

        x_test = np.array(x_test)

        # Изменение формы данных для LSTM
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

        # Получение прогнозов
        predictions = model.predict(x_test)
        predictions = scaler.inverse_transform(predictions)

        # Вывод численных значений предсказаний на следующий временной период и их доверительного интервала
        latest_data = test_data[-1].reshape(1, -1, 1)
        latest_prediction = model.predict(latest_data)
        latest_prediction = scaler.inverse_transform(latest_prediction)

        # Округление значений до двух знаков после запятой
        latest_prediction = round(latest_prediction[0, 0], 2)

        return latest_prediction

