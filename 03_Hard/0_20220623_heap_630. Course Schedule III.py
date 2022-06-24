from typing import List
##should check heap

class Solution: #not working
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        #sort the last day first
        def takeSecond(elem):
            return elem[1]
        courses.sort(key = takeSecond) #sorted(courses, key = lambda x:x[1])
        # print(courses) #[[100, 200], [1000, 1250], [200, 1300], [2000, 3200]]
        # print(courses[0][0], courses[0][1])

        CanTake = []
        for i in range(len(courses)):
            tempArr = []
            for j in range(i):
                tempArr.append(courses[j][0])
            
            n = sum[tempArr]
            m = courses[i][1]
            if n <= m:
                CanTake.append(courses[i][0])
        
        return len(CanTake)  

import heapq

class Solution2:      
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        course = []
        # sortedcourse = sorted(courses, key = lambda x:x[1])
        # print(sortedcourse)
        for i in sorted(courses, key = lambda x:x[1]):
            course.append(i[0])
            while sum(course) > i[1]:
                course.remove(max(course))
        return len(course)


if __name__ == '__main__':
    sol = Solution2()
    courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
    print(sol.scheduleCourse(courses))