#!/usr/bin/env python
#Game developed by Milad Rastian (miladmovie atsign gmail dot com) 
#http://weblog.miladmovie.com/
#I wrote this Game for course Artificial Intelligent in Yazd Jahad University
#Thanks my teacher Mr Asghar Dehghani
#I in this project I know how much I Love Python !
#Copyright (C) 2006  Milad Rastian
#
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#Read more about GNU General Public License :http://www.gnu.org/licenses/gpl.txt
import os, pygame,math
from pygame.locals import *
from Player import *
from inits import  *
from  Card import *
class background:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500,450),1)
        
        self.playedCards=[]
        self.tmpPlayedCard=[]
        self.errorMsg=""
        self.isPlayHeart=False
        pygame.display.set_caption('Hearts - beta 0.1')

                
        
       
        #reset hands
        self.playAgain()
        
        
        #set 
        #pygame.display.flip()  
        
        
        self.emptyGround=False
   

        self.screen.fill((0x00, 0xb0, 0x00))
        #self.drawCardsInHand()
        #bac,rc=load_image("j.gif")
        #self.screen.blit(bac,(290,150))
        
        pygame.display.flip() 
        
        self.numOfDeckPlay=0         
        self.players=[]
        self.players.append(self.player1)
        self.players.append(self.player2)
        self.players.append(self.player3)
        self.players.append(self.player4)
        #pygame.time.delay(5000)
       # import sys
        #sys.exit()
        indD=0
        while 1:         
            if self.numOfDeckPlay==13:
                print ""
                print ""
                print ""
                print self.player1.name," get ",self.player1.result," point"
                print self.player2.name," get ",self.player2.result," point"
                print self.player3.name," get ",self.player3.result," point"
                print self.player4.name," get ",self.player4.result," point"
                print ""
                print ""
                print ""
                self.playAgain()
            indD+=1
            if self.turnPlay==1 and self.player1.currentPlay==None:
                self.selectedCard=self.player1.play(self.tmpPlayedCard,self.playedCards,self.numOfDeckPlay,self.players)

                self.player1.currentPlay=self.selectedCard
                self.moveCardSlowly(self.selectedCard,screenPlayer1[14])
                self.tmpPlayedCard.append([self.selectedCard,1])
                #print "Player 1 play ",self.selectedCard.name
                self.selectedCard=None
                
                
            elif self.turnPlay==2 and self.player2.currentPlay==None:
                self.selectedCard=self.player2.play(self.tmpPlayedCard,self.playedCards,self.numOfDeckPlay,self.players)
                self.player2.currentPlay=self.selectedCard
                self.moveCardSlowly(self.selectedCard,screenPlayer2[14])
                self.tmpPlayedCard.append([self.selectedCard,2])
                #print "Player 2 play ",self.selectedCard.name
                self.selectedCard=None
                #pygame.time.delay(500)
            elif self.turnPlay==3 and self.player3.currentPlay==None:
                self.selectedCard=self.player3.play(self.tmpPlayedCard,self.playedCards,self.numOfDeckPlay,self.players)
                self.player3.currentPlay=self.selectedCard
                self.moveCardSlowly(self.selectedCard,screenPlayer3[14])
                self.tmpPlayedCard.append([self.selectedCard,3])
                #print "Player 3 play ",self.selectedCard.name
                self.selectedCard=None
                #pygame.time.delay(500)
                                               
            for event in pygame.event.get():
                if event.type == QUIT:
                    return  
                if event.type==MOUSEBUTTONDOWN:
                   if event.button==1:
                       if self.player4.currentPlay==None and self.turnPlay==4:
                           self.selectedCard=self.selectedCard=self.getCard(event.pos[0],event.pos[1])
                           if self.selectedCard:
                               if self.checkPlayCard(self.selectedCard,self.player4)==False:
                                   self.selectedCard=None
                                   break
                               
                               self.moveCardSlowly(self.selectedCard,screenPlayer4[14])
                               #self.selectedCard.isPlayed=True
                               self.player4.currentPlay=self.selectedCard
                               
                               self.tmpPlayedCard.append([self.selectedCard,4])
                               #print "Player 4 play ",self.selectedCard.name
                               #self.selectedCard=None
                           
                           
                       #print event.pos[0],event.pos[1]
                       #self.player4.moveAndShowCard(0,0, 0,self.screen)
                           
                   elif  event.button == 3:
                       self.selectedCard=self.selectedCard=self.getCard(event.pos[0],event.pos[1]) 
                       #try to show pop selected Card
                       if self.selectedCard:
                           self.selectedCard.goUp(self.screen)
                           pygame.display.flip() 
                           pygame.time.delay(500)
                           pass
                if   event.type==MOUSEBUTTONUP:
                    if event.button == 3:
                        if self.selectedCard:
                            if self.selectedCard.isPlayed==False:
                                #try do put hands of Player4 again
                                for i in range(0,13):
                                    if self.player4.cardsInHand[i].isPlayed==False:
                                        self.player4.moveCard(i,screenPlayer4[i][0], screenPlayer4[i][1])
            
            if self.player1.currentPlay!=None   and self.player2.currentPlay!=None   and self.player3.currentPlay!=None   and self.player4.currentPlay!=None  :
                #palyed on deck so we put ground in  PlayedCards
                self.player1.currentPlay.isPlayed=True
                self.player2.currentPlay.isPlayed=True
                self.player3.currentPlay.isPlayed=True
                self.player4.currentPlay.isPlayed=True
                self.addPlayedCards(self.player1.currentPlay, self.player2.currentPlay, self.player3.currentPlay, self.player4.currentPlay)
                self.turnPlay=self.howTurnNow(self.player1.currentPlay, self.player2.currentPlay, self.player3.currentPlay, self.player4.currentPlay)
                
                #check result on this deck
                typeToPlayed=self.tmpPlayedCard[0][0].type
                numOfMaxPlayed=self.tmpPlayedCard[0][0].name
                cardBelongToPlayer=None
                for i in range(0,4):
                    if self.tmpPlayedCard[i][0].type==typeToPlayed and  self.tmpPlayedCard[i][0].name>=numOfMaxPlayed:
                        numOfMaxPlayed=self.tmpPlayedCard[i][0].name
                        if self.tmpPlayedCard[i][1] ==1:
                            cardBelongToPlayer=self.player1
                        elif self.tmpPlayedCard[i][1]==2:
                            cardBelongToPlayer=self.player2
                        elif self.tmpPlayedCard[i][1]==3:    
                            cardBelongToPlayer=self.player3
                        elif self.tmpPlayedCard[i][1]==4:
                            cardBelongToPlayer=self.player4
                if cardBelongToPlayer:
                    result=0
                    for card in self.tmpPlayedCard:
                        if card[0].type==cardType.Hearts:
                            result+=1
                        if card[0].type==cardType.Spades and card[0].name==cardNumber.queen:
                            result+=13
                    cardBelongToPlayer.result+=result
                    print cardBelongToPlayer.name," get ",result," point"
                    cardBelongToPlayer=None
                    
                else:
                    print "Error !"
                
                #now set None to play next deck
                self.player1.currentPlay=None
                self.player2.currentPlay=None
                self.player3.currentPlay=None
                self.player4.currentPlay=None
                
                self.numOfDeckPlay+=1
                self.tmpPlayedCard=[]
                
                
            else:
                if self.turnPlay==1 and self.player1.currentPlay!=None:
                    self.turnPlay=2
                if self.turnPlay==2 and self.player2.currentPlay!=None:
                    self.turnPlay=3
                if self.turnPlay==3 and self.player3.currentPlay!=None:
                    self.turnPlay=4
                if self.turnPlay==4 and self.player4.currentPlay!=None:
                    self.turnPlay=1
            

            #if   event.type!=MOUSEBUTTONDOWN and event.button == 3 :
            self.screen.fill((0x00, 0xb0, 0x00))
            self.drawCardsInHand()

            if self.turnPlay==1:
                self.showMessage("Waiting for palyer 1 to play")
            if self.turnPlay==2:
                self.showMessage("Waiting for palyer 2 to play")
            if self.turnPlay==3:
                self.showMessage("Waiting for palyer 3 to play")
            if self.turnPlay==4:
                if self.errorMsg :
                    self.showMessage(self.errorMsg)
                else :
                    self.showMessage("Waiting for you to play! Come on harryup")
                pass
                        
            pygame.display.flip()                 
            pygame.time.delay(1000)
                   # self.screen.blit(background, (30, 40))
            # DRAWING             
            
            #self.cardGroup.draw(self.screen)
    #check how is turn now
    def howTurnNow(self,card1,card2,card3,card4):
        getMaxCardOfDeckPlay=self.tmpPlayedCard[0][0]
        turn=1
        if (card1.type==getMaxCardOfDeckPlay.type):
            if(card1.name>=getMaxCardOfDeckPlay.name):
                turn=1
                getMaxCardOfDeckPlay=card1
        if (card2.type==getMaxCardOfDeckPlay.type):
            if(card2.name>=getMaxCardOfDeckPlay.name):
                turn=2
                getMaxCardOfDeckPlay=card2
        if (card3.type==getMaxCardOfDeckPlay.type):
            if(card3.name>=getMaxCardOfDeckPlay.name):
                turn=3
                getMaxCardOfDeckPlay=card3
        if (card4.type==getMaxCardOfDeckPlay.type):
            if(card4.name>=getMaxCardOfDeckPlay.name):
                turn=4
                getMaxCardOfDeckPlay=card4
        return turn
                

    def checkIsPlayHeart(self):
        for i in range(0,len(self.playedCards)):
            for j in range(0,4):
                if self.playedCards[i][j].type==cardType.Hearts:
                    self.isPlayHeart=True
                    return            
    #check Players Play Correct Card
    def checkPlayCard(self,cardToPlay,player):
        if(self.isPlayHeart==False):
            self.checkIsPlayHeart()
        if(self.numOfDeckPlay==0):
            if len(self.tmpPlayedCard)==0:
                if cardToPlay.type==cardType.Clubs:
                    if cardToPlay.name==cardNumber.num2 :
                        return True
                self.errorMsg="You Must Start Game with 2 Clubs, Come on Don't Be Stupid !"
                return False
            if(cardToPlay.type==cardType.Hearts):
                self.errorMsg="In First Deck You Can not Play With Hearts, Do You Know How To Play?"
                return False
            if(cardToPlay.type==cardType.Spades and cardToPlay.name==cardNumber.queen):
                self.errorMsg="In First Deck You Can Not Play With Queen Of Spades , Do You Know How To Play? "
                return False
        if len(self.tmpPlayedCard)==0:
            if(self.isPlayHeart==False  and cardToPlay.type==cardType.Hearts):
                self.errorMsg="You Can Not Play Hearts Now ! Take Another Card"
                return False
        else:
            if cardToPlay.type!=self.tmpPlayedCard[0][0].type:
                if player.hastThisType(self.tmpPlayedCard[0][0].type):
                    self.errorMsg="Check Your Card To Play,You Should Play Card As Type First Deck"
                    return False
        if(cardToPlay.type==cardType.Hearts) :     
            self.isPlayHeart=True


        self.errorMsg=None
        return True
        
    def moveCardSlowly(self,moveCard,toLocation):
        #it will in to do list !
        #now just move straitly
        self.screen.fill((0x00, 0xb0, 0x00))
        moveCard.moveCard(toLocation[0],toLocation[1])
        #moveCard.moveCard(0,0)
        self.drawCardsInHand()                           
        #pygame.display.flip()  
        pygame.display.flip()
        pygame.time.delay(500)
        
    def drawCardsInHand(self):
        #draw cards of player1    
        self.player1.refreshHand(self.screen)

                 
        #draw cards of player2
        self.player2.refreshHand(self.screen)
        #draw cards of player3
        self.player3.refreshHand(self.screen)        
        #draw cards of player4
        self.player4.refreshHand(self.screen) 
 
    def showMessage(self,message,error=False):
        font = pygame.font.Font(None, 20)
        text = font.render(message, 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.screen.get_rect().centerx
        if error==False:
            self.screen.blit(text, (40,400))
        elif error==True:
            self.screen.blit(text, (50,450))
    def addPlayedCards(self,cardP1,cardP2,cardP3,cardP4):
        self.playedCards.append([cardP1,cardP2,cardP3,cardP4])
        
    def playAgain(self):
        self.playedCards=[]
        self.tmpPlayedCard=[]
        cc=cards()
        self.numOfDeckPlay=0
        self.player1=Player("Player1",0);
        self.player2=Player("Player2",1);
        self.player3=Player("Player3",2);
        self.player4=Player("Player4",3,True)
        cc.deck(self.player1, self.player2, self.player3, self.player4)
        self.putGround(self.player1,self.player2,self.player3,self.player4)   
        
        #check how has card 2 Clubs to first play
        if self.player1.has2Clubs==True:
            self.turnPlay=1
        if self.player2.has2Clubs==True:
            self.turnPlay=2
        if self.player3.has2Clubs==True:
            self.turnPlay=3
        if self.player4.has2Clubs==True:
            self.turnPlay=4
            
            
    def putGround(self,player1,player2,player3,player4):
        
        #sort hands of player1
        #player1.sortHande()
        #put cards of player1
        for i in range(0,13):  
            #background=player1.getCardImg(i) 
            player1.moveAndShowCard(i,screenPlayer1[i][0],screenPlayer1[i][1],self.screen)
            #self.screen.blit(background, (screenPlayer1[i][0], screenPlayer1[i][1]))
            
        #sort hands of player2
        #player2.sortHande()                 
        #put cards of player2
        for i in range(0,13):        
            player2.moveAndShowCard(i,screenPlayer2[i][0], screenPlayer2[i][1],self.screen)
            
        
        #sort hands of player3
        #player3.sortHande()
        #put cards of player3
        for i in range(0,13):        
            player3.moveAndShowCard(i,screenPlayer3[i][0], screenPlayer3[i][1],self.screen)
            
        #sort hands of player4
        player4.sortHande()
        #put cards of player4
        for i in range(0,13):
            player4.moveAndShowCard(i,screenPlayer4[i][0], screenPlayer4[i][1],self.screen)
        
        
        
    def getCard(self,x,y):
        for i in range(len(self.player4.cardsInHand)-1,-1,-1)  :
            if self.player4.cardsInHand[i].rect.collidepoint(x, y):
                fc = self.player4.cardsInHand[i]
                #print fc.name,fc.type
                
               
                return fc
        return None
            
def main():
    g = background()
    #g.mainLoop()

 
#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()       
