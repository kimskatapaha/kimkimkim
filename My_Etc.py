import maya.cmds as cmds

#뭐지
cmds.move (3,0,0)
cmds.rotate (0,70,0)



#정규식= [ ( 변수를 활용한 값 ) for ( 사용할 변수 이름 ) in ( 순회할 수 있는 값 )]
size = 10
arr = [0] * size
for i in range(len(size)):
    arr[i] = i * 2


size = 10
arr = [i * 2 for i in range(size)]

#람다= [ lambda (매개변수) : (표현식) ]
def hap(x, y):
    return x + y

hap(10, 20)


(lambda x,y: x + y)(10, 20)


mylist2 = sorted(mylist, key=lambda x: len(x))
print(mylist2)
#다음    . . . . . .


