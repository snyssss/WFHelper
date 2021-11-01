from flask import Flask
from wsgiref.simple_server import make_server
from server.Router import setRouter
from utils.ADBUtil import adbUtil
from utils.LogUtil import Log


class Server():
    app = Flask(__name__)
    wfhelper = None

    def __init__(self,wfhelper):

        # TODO 提供参数指定host和port
        self.main = wfhelper
        setRouter(self)


    def getLastLog(self):
        return Log.lastLog

    def getScreenShot(self):
        return adbUtil.getScreen()

    def touchScreen(self,x,y):
        adbUtil.touchScreen([x,y,x+1,y+1])

    def stopWFHelper(self):
        self.wfhelper.stop()

    def startWFHelper(self):
        self.wfhelper.isRunning = True


    def startServer(self):
        server = make_server('', 8080,self.app)
        server.serve_forever()
        # self.app.run("0.0.0.0",8080,debug=False)

        