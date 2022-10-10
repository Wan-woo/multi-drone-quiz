import time
from result import *

class ESDF:

    #Row = 0
    #Col = 0
    #obstacle_dict = {}
    

    def __init__(self, M, N, obstacle_list) -> None:
        self.Row = M 
        self.Col = N
        self.obstacle_dict = {}
        # Trying to initialize a obstacle dictionary, key = each col, value = [row number where obstacle is located]
        # Key will become p in next steps, and it will be easy to compute f on each row
        for val in obstacle_list:
            row = val[0]
            col = val[1]
            if col in self.obstacle_dict.keys():
                self.obstacle_dict[col].append(row)
            else:
                self.obstacle_dict[col] = []
                self.obstacle_dict[col].append(row)

    def intersection(self, P, P_value, Q, Q_value):
        return ((P_value + P * P) - (Q_value + Q * Q)) / (2 * (P - Q))

    def esdf_one_dimension(self, row_index):
        k = 0   # current parabola
        v = []  # (location, fvalue) of parabola
        z = []  # locations of boundaries
        distance_list = []
        
        # grid range [0, col-1] Z range [-1, col]
        # z.append(-1)
        # z.append(self.Col)

        # Compared to pesudocode mentioned in paper, problem arises when there are two obstacles with same col number but on different rows
        # To avoid that, v[i] needs to be a tuple (p, f)
        # Initialize v from -1 rather than 0, cause some obstacles may stand at (0, f)
        # v.append((-1, 0))
        # print("v[0][1] is"+str(v[0][1]))
        # key need to be ordered 
        
        for key in sorted(self.obstacle_dict.keys()):
            col_obstacle_list = self.obstacle_dict[key]
            # if multiple row applies, only select the one that is cloest to row_index
            f_list = [pow(abs(i-row_index),2) for i in col_obstacle_list]
            f_list.sort()
            # P > Q
            P = key
            P_value = f_list[0]
            if len(v) == 0:
                # just push first probola
                v.append((P, P_value))
                continue
            s = self.intersection(P, P_value, v[k][0], v[k][1])
       
            if len(z) == 0:
                z.append(s)
                k = k + 1
                v.append((P, P_value))
                continue
            while s <= z[k-1]:
                k = k - 1
                v = v[:-1]
                z = z[:-1]
                s = self.intersection(P, P_value, v[k][0], v[k][1])
                if len(z) == 0:
                    break
            # s > z[k]
            k = k + 1
           
            v.append((P, P_value))  #v[k] = (P, P_value)
            
            z.append(s)
            #z[k + 1] = self.Col
       
        k = 0
        for i in range(self.Col):
            # z[k] < 0, no need to compare
            while k < len(z) and z[k] <= i:
                k = k + 1
            distance_list.append((pow(i - v[k][0], 2) + v[k][1])**0.5)
        
        return distance_list

    def esdf_multi_dimension(self):
        result_list = []
        for row_index in range(self.Row):
            result_list.append(self.esdf_one_dimension(row_index))
        return result_list

def esdf(M, N, obstacle_list):
    """
    :param M: Row number
    :param N: Column number
    :param obstacle_list: Obstacle list
    :return: An array. The value of each cell means the closest distance to the obstacle
    """
    # 
    pass 


if __name__ == '__main__':
    st = time.time()
    for _ in range(int(2e4)):
        esdf_1 = ESDF(M=3, N=3, obstacle_list=[[0, 1], [2, 2]])
        assert np.array_equal(esdf_1.esdf_multi_dimension(), res_1)
        esdf_2 = ESDF(M=4, N=5, obstacle_list=[[0, 1], [2, 2], [3, 1]])
        assert np.array_equal(esdf_2.esdf_multi_dimension(), res_2)

    et = time.time()
    print(et-st)
