class Solution:
    def simplifyPath(self, path: str) -> str:
        que=['/']
        dotstack=0
        name=''
        
        for i in range(len(path)-1):
           if path[i]=='/':
               if name=='.':
                   name=0
                   continue
               if name=='..':
                   if len(que)>1:
                    que.pop()
                    que.pop()
                   continue
               if name!='':
                   que.append(name)

            else:
                      
        if que[-1]=='/' and len(que)!=1 and name=='':
            que.pop()
        if dotstack==1 and path[-1]=='.':
            if len(que)>1:
                print(que)
                que.pop()
                que.pop()
                print(que)
                dotstack=0
        if path[-1]!='/':
            name+=path[-1]
            que.append(name)
        ret=''
        print(que)
        for i in que:
            ret+=i
        return ret
            

                