
import matplotlib.pyplot as plt
# import numpy as np

def cp(data):
    cp_data = data['cp']
    print("Total Chest Pain Data and Diseased Chest Pain Data")
    plt.figure(3)
    plt.subplot(2,1,1)
    plt.hist(cp_data)
    plt.title('Total Chest Pain Data')
    plt.ylabel('Number of Person')
    plt.xticks([0,1, 2, 3],['', '', '', ''])

    true_cp_data = data[data.target==1]['cp']
    plt.subplot(2,1,2)
    plt.hist(true_cp_data)
    plt.title('Diseased Chest Pain Data')
    plt.xlabel('Chest Pain')
    plt.ylabel('Number of Person')
    plt.xticks([0, 1, 2, 3])
    plt.show()

if __name__=="__main__":
    cp()