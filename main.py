# Bad Apple!! demo on python
#
# crop video into frames:
# `ffmpeg -i bad_apple.mp4 -qscale:v 1 f%04d.png`



from PIL import Image
from time import sleep



FRAME_W_MAX = 480
FRAME_H_MAX = 360

FRAME_H = 20
FRAME_W = FRAME_H * FRAME_W_MAX // FRAME_H_MAX

FRAMES_AMOUNT = 6572

THRESHOLD = 127



def pixel_to_symbol(pixel: list) -> str:
    if pixel[0] >= THRESHOLD or pixel[1] >= THRESHOLD or pixel[2] >= THRESHOLD:
        return '@@'
    else:
        return '  '



def get_file_name(i: int) -> str:
    file_name = 'f'
    if 1 <= i < 10:
        file_name += '000'
    elif 10 <= i < 100:
        file_name += '00'
    elif 100 <= i < 1000:
        file_name += '0'
    elif 1000 <= i < FRAMES_AMOUNT:
        pass
    file_name += str(i) + '.png'
    return file_name


def load_frame(i: int) -> list:
    file_name = get_file_name(i)
    return Image.open('../../rust/data/frames/'+file_name)



def get_frame_as_str(i: int) -> str:
    frame = load_frame(i+1)
    frame_str = ''
    for h in range(FRAME_H):
        for w in range(FRAME_W):
            pixel = frame.getpixel((w * FRAME_W_MAX // FRAME_W, h * FRAME_H_MAX // FRAME_H))
            frame_str += pixel_to_symbol(pixel)
        frame_str += '\n'
    frame_str = frame_str[:-1]
    return frame_str



def main():
    for i in range(0, FRAMES_AMOUNT):
        frame_str = get_frame_as_str(i)
        print(5*'\n' + frame_str, end='')
        sleep(0.5 * 1/30)



if __name__ == '__main__':
    main()
    print('finished')



