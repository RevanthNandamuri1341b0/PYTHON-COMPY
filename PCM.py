from sys import stdin



def pcm_detect(st):
    if(st=="PCM" or st=="PMC" or st=="MPC" or st=="MCP" or st=="CMP" or st=="CPM"):
        print("YES ")
    else:
        print("NO ")

    # write your code here
num = input()
num=int(num)
i=0;
s=[]
for i in range(num):
    st=eval(stdin.readline())
    s.append(st)

j=0;
while (j<num):
    pcm_detect(s[j])
    j+=1