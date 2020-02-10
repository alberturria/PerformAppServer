from waves.interfaces.use_cases.draw_rms_use_case_interface import DrawRMSUseCaseInterface
from waves.repositories.get_rms_data_access import GetRMSDataAccess
import matplotlib.pyplot as plt


class DrawRMSUseCase(DrawRMSUseCaseInterface):
    def __init__(self, wave_id):
        self.wave_id = wave_id

    def run(self):
        get_rms_data_access = GetRMSDataAccess(self.wave_id)
        x_values = get_rms_data_access.get_rms()
        y_values = []
        for value in x_values:
            y_values.append(x_values.index(value))

        plt.plot(y_values, x_values)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')

        plt.title('Wave')

        plt.show()
