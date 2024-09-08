class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # Since it is a DSF problem use a stack. So if you are visting a room
        # keep all the keys in the room in a stack. And now try to vist the rooms
        # which you have keys to in the stack(pop them). Each time you vist a new
        # room add it to the visited set. Once the stack is empty check the length
        # of the visited set and total rooms if they are equal return true else false
        stack = []
        def stackPush(num,visited):
            for i in rooms[num]:
                if i not in visited:
                    stack.append(i)

        
        visited = set()
        
        visited.add(0)
        stackPush(0,visited)
        while stack:
            key = stack.pop()
            if key not in visited:
                visited.add(key)
                stackPush(key,visited)

        
        print(visited)
        if len(visited) == len(rooms):
            return True
        else:
            return False

        