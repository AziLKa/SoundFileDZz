from pydub import AudioSegment
# Импортирует модуль pydub, который позволяет работать с аудиофайлами в Python.
wav_file = AudioSegment.from_wav("music.wav")
# переносим ауидо файл в переменную

def speed_change(sound, speed=1.0):
# функция, для того что бы принять ауидо файл и коофициент скорости как аргументы, что бы работать с ними ехех
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    # новый ауидофайл с измененной частотой кадров
    # Строка использует метод _spawn библиотеки pydub для создания нового аудиофайла на основе исходного. Значение overrides используется для изменения частоты кадров
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)
    # Возвращает новый аудиофайл со скорректированной частотой кадров, которая была установлена в предыдущей строке.
    # Метод set_frame_rate устанавливает исходную частоту кадров для нового аудиофайла.

print('Замедлить или Ускорить? \nКоэффициенты ускорения: (1.5; 2; 3 и тп ) \nКоэффициенты замедления:( 0.5; 0.7; 0.8 и тп )')

user_input = input('Введите коэффициент: ')

fast_sound = speed_change(wav_file, float(user_input))
#  Вызывает speed_change с аргументами wav_file и user_input, и сохраняет результат в переменную fast_sound.
fast_sound.export("output.wav", format="wav")
#  экспортn