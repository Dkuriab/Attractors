import numpy
import pylab

from matplotlib.widgets import Slider


def chen_lee(x, y, z, a, b, c):
    # print(a, b, c)
    try:
        x_dot = a * x - y * z
        y_dot = b * y + x * z
        z_dot = c * z + x * y / 3
    except RuntimeError:
        return 0.1, 0.1, 0.1

    return x_dot, y_dot, z_dot


if __name__ == '__main__':
    def update():
        try:
            global slider_a
            global slider_b
            global slider_c
            global graph_axes

            a = slider_a.val
            b = slider_b.val
            c = slider_c.val

            dt = 0.01
            num_steps = 10000

            xs = numpy.empty(num_steps + 1)
            ys = numpy.empty(num_steps + 1)
            zs = numpy.empty(num_steps + 1)

            xs[0], ys[0], zs[0] = (0.1, 0.1, 0.1)

            for i in range(num_steps):
                x_dot, y_dot, z_dot = chen_lee(xs[i], ys[i], zs[i], a, b, c)
                xs[i + 1] = xs[i] + (x_dot * dt)
                ys[i + 1] = ys[i] + (y_dot * dt)
                zs[i + 1] = zs[i] + (z_dot * dt)

            graph_axes.clear()

            graph_axes.plot(xs, ys, zs, lw=0.5)
            pylab.draw()

        except RuntimeWarning:
            return


    def on_change(value):
        update()


    fig = pylab.plt.figure()

    graph_axes = fig.add_subplot(111, projection='3d')

    fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.4)

    axes_slider_a = pylab.axes([0.05, 0.25, 0.85, 0.04])
    slider_a = Slider(axes_slider_a,
                      label='a',
                      valmin=0.3,
                      valmax=1.9,
                      valinit=1.5,
                      valfmt='%1.2f')

    slider_a.on_changed(on_change)

    axes_slider_b = pylab.axes([0.05, 0.17, 0.85, 0.04])
    slider_b = Slider(axes_slider_b,
                      label='b',
                      valmin=-11.,
                      valmax=-9.4,
                      valinit=-10.,
                      valfmt='%1.2f')
    slider_b.on_changed(on_change)

    axes_slider_c = pylab.axes([0.05, 0.09, 0.85, 0.04])
    slider_c = Slider(axes_slider_c,
                      label='c',
                      valmin=-0.4,
                      valmax=0.,
                      valinit=-0.38,
                      valfmt='%1.2f')

    slider_c.on_changed(on_change)

    update()
    pylab.show()
