class AlarmClock:

    def __init__(self, currHrs, currMinutes, alarmTime=0, alarmSound="Loud Beep"):
        self.currHrs=currHrs
        self.currMinutes=currMinutes
        self.alarmTime=alarmTime
        self.alarmSound=alarmSound

        self.alarm=self.soundAlarm()

    def soundAlarm(self):
        if(self.getCurrTime()==self.alarmTime):
            self.alarm="on"
        else:
            self.alarm="off"

    def getCurrTime(self):

        if(self.currMinutes==0):
            currMinutes="00"
        else:
            currMinutes=self.currMinutes
        
        return str(self.currHrs)+":"+str(currMinutes)

    def addMinute(self):
        self.currMinutes+=1

        if(self.currMinutes==60):
            self.currHrs+=1
            self.currMinutes=0

        if(self.currHrs==13):
            self.currHrs=1


