import matplotlib.pyplot as plt
import numpy as np

def age(data):
    age_data = data['age']
    print("Total Age Data| Count:"+str(len(age_data)))
    print("Minimum age:"+str(min(age_data)))
    print("Maximum age:"+str(max(age_data)))
    print("Average age:"+str(np.mean(age_data)))
    print("Median age:"+str(np.median(age_data)))

    sorted_age = np.sort(age_data)
    plt.figure(0)
    plt.hist(age_data, bins = 8)
    plt.title('Total Age Data')
    plt.xlabel('Age')
    plt.ylabel('Number of Person')
    plt.show()

    true_age_data = data[data.target==1]['age']
    print("Diseased Age Data| Count:"+str(len(true_age_data)))
    print("Minimum age:"+str(min(true_age_data)))
    print("Maximum age:"+str(max(true_age_data)))
    print("Average age:"+str(np.mean(true_age_data)))
    print("Median age:"+str(np.median(true_age_data)))

    sorted_age = np.sort(true_age_data)
    plt.figure(1)
    plt.hist(true_age_data, bins = 8)
    plt.title('Diseased Age Data')
    plt.xlabel('Age')
    plt.ylabel('Number of Person')
    plt.show()

if __name__=="__main__":
    age()