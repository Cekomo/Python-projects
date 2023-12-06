import numpy as np
import matplotlib.pyplot as plt

class OscillationGenerator():
    def __init__(self) -> None:
        self.point_array = []
        self.start_point = 0


    def draw_custom_line(self, sample_size, start_point=0, frequency=1, magnitude=1):
        self.draw_oscillation(sample_size, start_point, frequency, magnitude)

        plt.plot(self.point_array)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Matplotlib Example')
        plt.show()

    def draw_oscillation(self, sample_size, start_point, frequency, magnitude):
        current_dot = start_point
        for dot in range(0, sample_size):
            sin_wave = magnitude * np.sin(frequency * dot)
            cos_wave = magnitude * 2 * np.cos(frequency * 0.8 * dot)
            # current_dot += temp
            self.point_array.append(sin_wave + cos_wave) 
            

oscillation_generator = OscillationGenerator()
oscillation_generator.draw_custom_line(2000, 0, 0.05,3)