from pwm_dac import PWM_DAC as pd
pwm=pd(12, 500, 3.3)
pwm.setvol(1.5)
