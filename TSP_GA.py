# -*- encoding: utf-8 -*-

import math
import random
import matplotlib.pyplot as plt
from GA import GA

class TSP(object):
      def __init__(self, aLifeCount = 100):
            self.initCitys()
            self.lifeCount = aLifeCount
            self.ga = GA(aCrossRate = 0.7, 
                  aMutationRage = 0.02, 
                  aLifeCount = self.lifeCount, 
                  aGeneLenght = len(self.citys), 
                  aMatchFun = self.matchFun())


      def initCitys(self, n=20):
            self.citys = []
            for i in range(n):
                  x = random.randint(0, 1000)
                  y = random.randint(0, 1000)
                  self.citys.append((x, y))


      def distance(self, order):
            distance = 0.0
            for i in range(-1, len(self.citys) - 1):
                  index1, index2 = order[i], order[i + 1]
                  city1, city2 = self.citys[index1], self.citys[index2]
                  distance += math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
            return distance


      def matchFun(self):
            return lambda life: 1.0 / self.distance(life.gene)


      def run(self, n = 0):
            self.plotcities()
            while n > 0:
                  self.ga.next()
                  distance = self.distance(self.ga.best.gene)
                  print (("%d : %f") % (self.ga.generation, distance))
                  n -= 1
            self.plotcities()

      def plotcities(self):
            plt.figure()
            plt.plot(self.citys[:][0], self.citys[:][1], 'b*')
            plt.plot(self.citys[:][0], self.citys[:][1], 'b')
            plt.plot([self.citys[-1][0], self.citys[0][0]], [self.citys[-1][1], self.citys[0][1]], 'b')


def main():
      tsp = TSP()
      tsp.run(100)
      print(tsp.ga.best.gene)


if __name__ == '__main__':
      main()


