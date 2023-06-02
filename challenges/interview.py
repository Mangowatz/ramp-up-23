#evaluate whether an interviewee is qualified or not

def interview(list,totalTime):
    if(len(list)<8):
        return "disqualified"
    if(list[0]>5 or list[1]>5):
        return "disqualified"
    if(list[2]>10 or list[3]>10):
        return "disqualified"
    if(list[4]>15 or list[5]>15):
        return "disqualified"
    if(list[5]>20 or list[6]>20):
        return "disqualified"
    if(totalTime>120):
        return "disqualified"
    return "qualified"

print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))
print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120))
print(interview([5, 5, 10, 10, 15, 15, 20], 120))
print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))