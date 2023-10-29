![Без названия (62) (1)](https://github.com/Omegon226/Service_Time_Series_Model_Creator/assets/69383841/6177c86c-ff7e-44a1-977c-d2c4584106f4)

# Проблема

Существует проблема в автоматизации создания моделей для предсказания временных рядов. Причём не просто их создания, но и подбор самых оптимальных гиперпараметров. Также существующие инструменты в крайне редких случаях предоставляют возможность имплементации внешних ML моделей. Уже существующие продукты не во всех случаях позволяют работать с данными, которые будут подаваться в модель. Мой проект создан, чтобы решить эти проблемы 

# Задачи

- Разработать API с которым могут взаимодействовать внешние системы
- Разработать удобный графический интерфейс для работы с бэкендои
- Внедрить возможность чтения данных с помощью множества способов
- Создать инструменты для работы с данными
- Осуществить возможность визуализаций данных с помощью различных инструментов
- Создать возможность автоматизации создания ML моделей для предсказания временных рядов на основе заданных гиперпараметров
- Предусмотреть, чтобы пользователь мог внедрить свои: ML модели, скейлеры, метреки для тестирования созданных моделей

## UseCase

![Use Case drawio](https://github.com/Omegon226/service_time_series_model_creator/assets/69383841/235503cb-60b2-438a-933e-b1ef0301b352)

# Что было сделано и Результаты

Разработан бэкенд (FastAPI) и фронтенд (Streamlit), который реализует вышеописанный функционал. Для работы с данными использовались: NumPy, Pandas. Для визуализаций: MatPlotLib и Seaborn (визуализации подавались через запросы в бинарном формате). Для организации работы с моделями были использованы: Scikit - Learn, Keras, Dill

Получившиеся модели обёртываются в так называемый ML Pipeline, который позволяет инкасулировать преобразования данных от подачи в модель до получения итоговых результатов. ниже представлена концепция ML Pipeline

![image](https://github.com/Omegon226/service_time_series_model_creator/assets/69383841/5f34559f-97b9-40e0-be0b-2741d44fd2b0)

Ниже представлен API сервиса, созданный с помощью Swagger-а и также Веб интерфейс созданный на Streamlit

![image](https://github.com/Omegon226/service_time_series_model_creator/assets/69383841/d8144e4b-aca5-4a12-9397-eb6c0f5c9a65)

![image](https://github.com/Omegon226/service_time_series_model_creator/assets/69383841/1449046e-f9dc-4c43-a36f-9137ddf37b10)

![image](https://github.com/Omegon226/service_time_series_model_creator/assets/69383841/68bfa2f5-cddc-432d-96ac-6120cb4f7e79)

# Библиотеки:

- FastAPI (pip install fastapi)
- Uvicorn (pip install "uvicorn[standard]")
- Streamlit (pip install streamlit)
- NumPy (pip install numpy)
- Pandas (pip install pandas)
- MatPlotLib (pip install matplotlib)
- Seaborn (pip install seaborn)
- Scikit - Learn (pip install scikit-learn)
- Joblib (pip install joblib)
- Keras (pip install keras)
- TensorFlow (pip install tensorflow)
- Dill (pip install dill)
- PyYAML (pip install pyyaml)
- Python-Multipart (pip install python-multipart)
- Request (pip install requests)
