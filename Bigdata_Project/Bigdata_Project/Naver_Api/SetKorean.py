from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
### 한국어 설정
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
fig = plt.figure()