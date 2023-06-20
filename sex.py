import matplotlib.pyplot as plt
# import numpy as np

def sex(data):
    sex_data = data['sex']
    print("Total Sex Data and Diseased Sex Data")
    plt.figure(2)
    plt.subplot(2,1,1)
    plt.hist(sex_data)
    plt.title('Total Sex Data')
    plt.ylabel('Number of Person')
    plt.xticks([0,1],['', ''])

    true_sex_data = data[data.target==1]['sex']
    plt.subplot(2,1,2)
    plt.hist(true_sex_data)
    plt.title('Diseased Sex Data')
    plt.xlabel('Sex')
    plt.ylabel('Number of Person')
    plt.xticks([0,1],['Female', 'Male'])
    plt.show()

if __name__=="__main__":
    sex()