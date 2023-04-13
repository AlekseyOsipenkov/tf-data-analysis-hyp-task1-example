import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 449719925 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
   
    significance = 0.07

    sample_success_a, sample_size_a = (x_success, x_cnt)
    sample_success_b, sample_size_b = (y_success, y_cnt)

    successes = np.array([sample_success_a, sample_success_b])
    samples = np.array([sample_size_a, sample_size_b])
    
    stat, p_value = proportions_ztest(count=successes, nobs=samples)

    if p_value > significance:
         return True
    else:
         return False
   
