# 
import time
import threading
import random
class Stop_and_Wait:
    acknowledgment = None
    recieved_data = []
    def reciever(self,frame):
        rand = random.random()
        #reducing the percentage of success by 40%
        if(rand<0.6):
            ob_frame = frame
            self.recieved_data.append(frame)
            return ob_frame
        return None
    def sender(self,frames):
        i = 0
        while i < len(frames):
            acknowledgment = self.reciever(frames[i])
            print('Sending:', frames[i])
            time.sleep(2)
            if acknowledgment is not None:
                print('received acknowledgment:', acknowledgment)
                if acknowledgment == frames[i]:
                    i += 1
                else:
                    print('Error')
            else:
                print('Timeout! Resending Frame:', frames[i])
    def run(self):
        data_frames = [1, 2, 3, 4, 5]
        sender_t = threading.Thread(target=self.sender, args=(data_frames,))
        sender_t.start()
        sender_t.join()

if __name__ == "__main__":
    stop_and_wait = Stop_and_Wait()
    stop_and_wait.run()


