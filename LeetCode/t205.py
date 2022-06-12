class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # map_s=map()
        map_s={}
        i=0
        maped=[]
        for ch in s:
            t_i=t[i]
            # map_ch=map_s[ch]
            print("======")
            print("t_i",t_i)
            if ch not in map_s:
            # if map_s[ch]==None:
                map_s[ch]=t_i
                print("map_s")
                print(map_s)
                maped.append(t_i)
            else:
                map_ch=map_s[ch]
                print("map_ch",map_ch)
                # if maped.con
                # t_i 另外一个 a: b ,c :b
                print("maped",maped)
                print("t_i",t_i)
                if t_i in maped:
                    return False
                if map_ch==t_i:
                    # 可以的
                    pass
            
                else:
                    return False

            i+=1

        return True

Solution=Solution()
res=Solution.isIsomorphic("badc","baba")

print("res")
print(res)
# ctrl b 打开旁边 左边列表