import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QPushButton
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qtagg import FigureCanvas
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


class DuffingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Duffing Equation Parameters')

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.parameter_labels = {
            'delta': QLabel('Delta'),
            'alpha': QLabel('Alpha'),
            'beta': QLabel('Beta'),
            'gamma': QLabel('Gamma'),
            'omega': QLabel('Omega')
        }

        self.sliders = {}
        for param, label in self.parameter_labels.items():
            slider = QSlider(Qt.Orientation.Horizontal)
            slider.setMinimum(-100)
            slider.setMaximum(100)
            slider.setValue(0)
            slider.setTickInterval(1)
            slider.setTickPosition(QSlider.TickPosition.TicksBelow)
            self.sliders[param] = slider

            layout.addWidget(label)
            layout.addWidget(slider)

        run_button = QPushButton('Run')
        run_button.clicked.connect(self.runSimulation)
        layout.addWidget(run_button)

        self.plot_figure = plt.figure()
        self.plot_canvas = FigureCanvas(self.plot_figure)
        layout.addWidget(self.plot_canvas)

    def runSimulation(self):
        delta = self.sliders['delta'].value() / 10.0
        alpha = self.sliders['alpha'].value() / 10.0
        beta = self.sliders['beta'].value() / 10.0
        gamma = self.sliders['gamma'].value() / 10.0
        omega = self.sliders['omega'].value() / 10.0

        # Solve Duffing equation
        t_span = (0, 100)
        y0 = [0.0, 0.0]
        sol = solve_ivp(lambda t, y: duffing(t, y, delta, alpha, beta, gamma, omega), t_span, y0, method='RK45', t_eval=np.linspace(t_span[0], t_span[1], 1000))

        # Clear previous plot
        self.plot_figure.clear()

        # Plot the solution
        ax = self.plot_figure.add_subplot(111)
        ax.plot(sol.t, sol.y[0], 'b', label='x(t)')
        ax.set_xlabel('Time')
        ax.set_ylabel('Displacement')
        ax.set_title('Duffing Equation with Sinusoidal Driving Force')
        ax.legend()
        ax.grid(True)

        # Update the canvas
        self.plot_canvas.draw()


def duffing(t, y, delta, alpha, beta, gamma, omega):
    x, v = y
    dxdt = v
    dvdt = -delta * v - alpha * x - beta * x**3 + gamma * np.cos(omega * t)
    return [dxdt, dvdt]


def main():
    app = QApplication(sys.argv)
    duffing_app = DuffingApp()
    duffing_app.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
