size = 7
def FCFS(arr, head):
 
    seek_count = 0
    distance, cur_track = 0, 0
 
    for i in range(size):
        cur_track = arr[i]
 
        # calculate absolute distance
        distance = abs(cur_track - head)
 
        # increase the total count
        seek_count += distance
 
        # accessed track is now new head
        head = cur_track
     
    print("Total number of seek operations = ",
                                   seek_count)
 
    # Seek sequence would be the same
    # as request array sequenc
    print("Seek Sequence is")
 
    for i in range(size):
        print(arr[i])
     
# Driver code
if __name__ == '__main__':
 
    # request array
    arr = [ 161, 189, 76, 45, 48, 31, 19 ]
    head = 100
 
    FCFS(arr, head)