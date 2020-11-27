from math import *
import random

def plane_angle_and_length(a, b):
    '''
    it finds all I need for my program please DON'T TOUCH
    :param a:
    :param b:
    :return:
    '''
    if a!=b:
        x = b[0] - a[0]
        y = b[1] - a[1]
        l = sqrt(x ** 2 + y ** 2)
        return [(asin(y / l) if x >= 0 else (pi - asin(y / l))), l]
    else:
        return 0, 0


def iter(coord1, coord2, angle_and_length_list, full_length):
    '''
    creates new iteration between two points
    :param coord1:
    :param coord2:
    :param angle_and_length_list:
    :param full_length:
    :return:
    '''
    new_list = [coord1]
    angle0, length0 = plane_angle_and_length(coord1, coord2)
    for angle, length in angle_and_length_list:
        old_x, old_y = new_list[-1]
        new_length = length * (length0 / full_length)
        new_x = old_x + cos(angle + angle0) * new_length
        new_y = old_y + sin(angle + angle0) * new_length
        new_list.append([new_x, new_y])
    return new_list[:-1]


def fractal_wall(time, length, vertex_number, iter_number, frequency, variation1, variation2):
    '''

    :param time: time or another smooth changing variable
    :param length: length of wall from first to last point
    :param vertex_number: number of vertexes between first and last point
    :param iter_number: depth of fractal recursion
    :param frequency: cycle frequency
    :param variation1: random number from 0 to 1
    :param variation2: random number from 0 to 1
    :return: coords of all points in fractal
    '''
    initial_list = [[0, 0]]

    l0 = length / (vertex_number + 1)
    for i in range(vertex_number):
        x = (l0 ) * sin(time * frequency) * cos(frequency * time * (variation1 * cos(sin(i * 2))) + i * 2 * pi / vertex_number) + l0 * (i + 1)
        y = (l0 ) * sin(frequency * time * (variation2 * cos(i + 3)) + i * 2 * pi / vertex_number)
        initial_list.append([x, y])
    initial_list.append([length, 0])
    initial_angle_and_length_list = []
    for i in range(vertex_number + 1):
        initial_angle_and_length_list.append(plane_angle_and_length(initial_list[i], initial_list[i + 1]))
    previous_list = initial_list
    for i in range(iter_number):
        new_list = []
        for k in range(len(previous_list) - 1):
            new_dots = iter(previous_list[k], previous_list[k + 1], initial_angle_and_length_list, length)
            for j in new_dots:
                new_list.append(j)
        previous_list = new_list
        previous_list.append([length, 0])
    return previous_list


if __name__ == '__main__':
    import tkinter
    v1 = 0.7
    v2 = 0.2
    master = tkinter.Tk()
    canvas = tkinter.Canvas(master, height=600, width=600)
    lines = []
    iters = 3
    vertex = 3
    time = 0
    all_coords = []
    list_of_lines = []
    lines_coords = fractal_wall(time, 400, 6, 2, 0.02, v1, v2)
    for i in range(len(lines_coords) - 1):
        list_of_lines.append(canvas.create_line([lines_coords[i][0] + 100, lines_coords[i][1] + 300],
                                                [lines_coords[i + 1][0] + 100, lines_coords[i + 1][1] + 300]))

    def game():
        global time
        time += 1
        lines_coords = fractal_wall(time, 400, 6, 2, 0.02, v1, v2)
        all_coords.append(lines_coords)
        for i in range(len(lines_coords) - 1):
            canvas.coords(list_of_lines[i],[lines_coords[i][0]+100, lines_coords[i][1] + 300,
                                                    lines_coords[i + 1][0]+100, lines_coords[i + 1][1] + 300])

        canvas.update()

        master.after(1, game)


    canvas.pack()
    game()
    master.mainloop()

