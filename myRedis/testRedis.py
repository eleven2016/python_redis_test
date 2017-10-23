'''
Created on 2017年6月27日

@author: ywl48338
'''
import redis
if __name__ == '__main__':
    connection=redis.Redis(host="localhost", port="6379", db=0)
    #connection.setex("test1", 1, 1)
    #print(connection.get("test1"))
    
    #connection.lpush("testList", 1,2,3,4,5,6,7)
    
    #print(connection.rpop("testList"))
    #print(connection.lrange("testList", 0, 6))
    
    #connection.sadd("testMap",'a',1,'b','c')
    #print(connection.smembers("testMap"))
    
    #print(connection.srem("testSet",'c','d'))
    #print(connection.smembers("testSet"))
    #print(connection.scard("testMap"))
    
    #connection.sadd("testSet1",'a','b','e','t')
    #print(connection.sunion("testSet1","testSet"))
    
    
    #connection.hmset("testMap", {"a":1,"b":2,"c":3})
    #print(connection.hkeys("testMap"))
    #print(connection.hmget("testMap", "a"))
    
    #connection.zadd("testZset",1.0,"a",2.0,"b")
    
    a=connection.pipeline(transaction=True)
    connection.setnx("testtransaction", 1)
    connection.lpush("testtransactionList", 1,2,3,4,5)
    
    a.execute()
    print(connection.get("testtransaction"))
    print(connection.lrange("testtransactionList", 0, 5))
    
    
    
    
    