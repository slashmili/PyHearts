#Game developed by Milad Rastian (miladmovie atsign gmail dot com) 
#http://weblog.miladmovie.com/
#I wrote this Game for course Artificial Intelligent in Yazd Jahad University
#Thanks my teacher Mr Asghar Dehghani
#I in this project I know how much I Love Python !
#Copyright (C) 2006  Milad Rastiann
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

from inits import  *

class Player:
    
    def __init__(self,name="",location=0,isHuman=False):
        self.isHuman=isHuman
        self.cardsInHand=[]
        self.currentPlay=None
        self.has2Clubs=False
        self.hasQueenSpades=False
        self.isPlayHeart=False
        self.isQueenSpadesPlayed=False
        self.result=0
        self.name=name
        self.locationInPlayedCard=location
        self.tryDontPlayHearts=False
        self.tryDontPlaySpades=False
        self.tryDontPlayDaimond=False
        self.tryDontPlayClubs=False
        
    def addHand(self,card):
        self.cardsInHand.append(card)
        card.index=len(self.cardsInHand)-1
        if card.name==cardNumber.num2 and card.type==cardType.Clubs:
            self.has2Clubs=True
        if card.name==cardNumber.queen and card.type==cardType.Spades:
            self.hasQueenSpades=True
    def analayzLastDeck(self,playedCard):
        
        #there is not any thing to analayz, dont waste my players time :P ;)
        if self.tryDontPlayHearts==True and self.tryDontPlayClubs==True and self.tryDontPlayDaimond==True and self.tryDontPlaySpades==True:
            return 
        for cards in playedCard:

            #check if in the last paly analayz dont do that again
            if cards[self.locationInPlayedCard].type==cardType.Hearts and self.tryDontPlayHearts==True:
                break
            if cards[self.locationInPlayedCard].type==cardType.Clubs and self.tryDontPlayClubs==True:
                break
            if cards[self.locationInPlayedCard].type==cardType.Daimond and self.tryDontPlayDaimond==True:
                break                
            if cards[self.locationInPlayedCard].type==cardType.Spades and self.tryDontPlaySpades==True:
                break    

            for card in cards:
                tryDontPlayType=False
                
                #check if know it players card dont check it            
                if card.type==cards[self.locationInPlayedCard].type and card.name==cards[self.locationInPlayedCard].name :
                    continue
                if card.type!=cards[self.locationInPlayedCard].type:
                    tryDontPlayType=True
                else:
                    tryDontPlayType=False
            if tryDontPlayType==True:
                if cards[self.locationInPlayedCard].type==cardType.Hearts:
                    self.tryDontPlayHearts=True
                elif cards[self.locationInPlayedCard].type==cardType.Clubs:
                    self.tryDontPlayClubs=True
                elif cards[self.locationInPlayedCard].type==cardType.Daimond:
                    self.tryDontPlayDaimond=True
                elif cards[self.locationInPlayedCard].type==cardType.Spades:
                    self.tryDontPlaySpades=True
            pass
    def play(self,cardInGround,playedCard,numOfDeckPlay):
        retcard=None
        #check is heart or Queen of Spades play yet ?
        self.checkIsPlayHeart(playedCard)
        self.analayzLastDeck(playedCard)
        #check if game played by hearts try play by less than cards in ground
        if len(cardInGround)!=0:
            if cardInGround[0][0].type==cardType.Hearts:
                #try to find max number of card in ground as type cardInGround[0][0].type
                tmpCardNumberMaxInGround=cardInGround[0][0].name
                for card in  cardInGround:
                    if card[0].name>tmpCardNumberMaxInGround and card[0].type==cardType.Hearts:
                        tmpCardNumberMaxInGround=card[0].name
                tmpCardNumberMaxInHand=0
                for card in self.cardsInHand:
                    if card.type==cardType.Hearts and card.name<tmpCardNumberMaxInGround and card.name>tmpCardNumberMaxInHand and card.isPlayed==False:
                            tmpCardNumberMaxInHand=card.name
                            retcard=card
                if retcard:
                    if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
                        return self.setAsPlay(retcard)
                    else:
                        retcard=None
        
        #if has Queen of Spades check this conditions
        if self.hasQueenSpades==True:                
            #check if has Queen of Spades and has not Type of Play Card, Play with Queen of Spades
            if len(cardInGround)!=0:
                #check if has not card type as cardInGround[0][0].type
                if self.hastThisType(cardInGround[0][0].type)==False:
                    #now try to find Queen of Spades
                    for card in self.cardsInHand:
                        if card.type==cardType.Spades and card.name==cardNumber.queen:
                            if self.checkPlayCard(card, cardInGround, numOfDeckPlay):
                                return self.setAsPlay(card)
                            else:
                                retcard=None                
                            break
            #check if his turn to bein game and has not Queen of Spades try to play with Spades less than Queen
            if self.checkIsPlayedQueen(playedCard)==False and len(cardInGround)==0 :
                if self.hastThisType(cardType.Spades)==True:
                    tmpCard=cardNumber.queen
                    for i in range(13):
                        if self.cardsInHand[i].isPlayed==False:
                            if self.cardsInHand[i].type==cardType.Spades and self.cardsInHand[i].name<tmpCard:
                                retcard=self.cardsInHand[i]
                                tmpCard=self.cardsInHand[i].name
                if retcard:
                    if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
                        return self.setAsPlay(retcard)
                    else:
                        retcard=None
            #check if has Queen of Spades and played  bigger than Queen Play Queen Now
            if len(cardInGround)!=0:
                if cardInGround[0][0].type==cardType.Spades:
                    tryToFindQueenOfSpades=False
                    for card in cardInGround:
                        if card[0].type==cardType.Spades and card[0].name>cardNumber.queen:
                            tryToFindQueenOfSpades=True
                            break
                    if tryToFindQueenOfSpades==True:
                        #try to find Queen of Spades  Card
                        for card in self.cardsInHand:
                            if card.name==cardNumber.queen and card.type==cardType.Spades:
                                retcard=card
                                if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
                                    return self.setAsPlay(retcard)
                                else:
                                    retcard=None
                                break
                
        #check if 
        #check if has not play Queen of Spades yet and in this ground has Queen play less than Queen of Spades
        if len(cardInGround)!=0  :
            if cardInGround[0][0].type==cardType.Spades:
                tryFindLessQueen=False
                for card in cardInGround:
                    if card[0].name>=cardNumber.queen and  card[0].type==cardType.Spades :
                        tryFindLessQueen=True
                        break
                if tryFindLessQueen==True:
                    tmpCardNum=0
                    for card in self.cardsInHand:
                        if card.type==cardType.Spades and card.name>tmpCardNum and card.name<cardNumber.queen and card.isPlayed==False :
                            retcard=card
                            tmpCardNum=card.name
                    if retcard:
                        if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
                            return  self.setAsPlay(retcard)
                        else:
                            retcard=None
        
        #check if has not card type to play play with bigger Hearts on hand
        if len(cardInGround)!=0   :
            if self.hastThisType(cardInGround[0][0].type)==False and self.hastThisType(cardType.Hearts)==True:
                maxNumOfHeartsInHand=0
                for card in self.cardsInHand:
                    if card.type==cardType.Hearts and card.name>maxNumOfHeartsInHand and card.isPlayed==False:
                        maxNumOfHeartsInHand=card.name
                        retcard=card
                if retcard:
                    if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
                        return  self.setAsPlay(retcard)
                    else:
                        retcard=None
                    
        #if is any card in ground try to find max in hand and min in ground    
        if len ( cardInGround )!=0:
            typeToPlay=cardInGround[0][0]
            maxNumToPlay=0
            for card in cardInGround:
                if card[0].type==typeToPlay and card[0].name>maxNumToPlay:
                    maxNumToPlay=card[0].name
            maxInHand=0
            for card in self.cardsInHand:
                if card.type==typeToPlay and card.name<maxNumToPlay and card.name>maxInHand and card.isPlayed==False :
                    maxInHand=card.name
                    retcard=card
            if retcard:
                if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
                    return  self.setAsPlay(retcard)
                else:
                    retcard=None
        #check if cards in ground and cannot find less than cards in ground, try to find less card to play
        if len(cardInGround)!=0:
            cardTypeToPlay=cardInGround[0][0].type
            cardNumberToPlay=cardInGround[0][0].name
            minCard=14
            for card in self.cardsInHand:
                if card.isPlayed==False and card.type==cardTypeToPlay and card.name<minCard :
                    minCard=card.name
                    retcard=card
            if retcard:
                if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
                    return  self.setAsPlay(retcard)
                else:
                    retcard=None
        
        #play in normall mode but try to use analayzed information
        if len(cardInGround)==0:
            for card in self.cardsInHand:
                if card.isPlayed==False:
                    if self.tryDontPlayHearts==True and card.type==cardType.Hearts: 
                        continue
                    if self.tryDontPlaySpades==True and card.type==cardType.Spades:
                        continue
                    if self.tryDontPlayDaimond==True and card.type==cardType.Daimond:
                        continue
                    if self.tryDontPlayClubs==True and card.type==cardType.Clubs:
                        continue
                    if self.checkPlayCard(card, cardInGround, numOfDeckPlay):
                        retcard=card
            if retcard:
                return self.setAsPlay(retcard)
        
                        
        #Ok stupid ! play every thinh you want ! I dont know how much must learn you Hearts Game
        for i in range(0,13):
            if self.cardsInHand[i].isPlayed==False:
                if self.checkPlayCard(self.cardsInHand[i], cardInGround, numOfDeckPlay):
                    retcard=self.cardsInHand[i]
        
        if retcard:
            return self.setAsPlay(retcard)
    
    def setAsPlay(self,card):
        card.isPlayed=True
        if card.name==cardNumber.queen and cardType.Spades==card.type:
            self.hasQueenSpades=False
        return card
        
    def checkIsPlayedQueen(self,playedCard):
        for i in range(0,len(playedCard)):
            for j in range(0,4):
                if playedCard[i][j].type==cardType.Spades and playedCard[i][j].name==cardNumber.queen:
                    return True
        return False
    
    

    def removeCards(self):
        self.cardsInHand
    def sortHande(self):

        for i in range(0,13):
            for j in range(0,13):
                if(self.cardsInHand[i].type>self.cardsInHand[j].type):
                    tmp=self.cardsInHand[i]
                    #self.cardsInHand[i]=None
                    self.cardsInHand[i]=self.cardsInHand[j]
                    #self.cardsInHand[j]=None
                    self.cardsInHand[j]=tmp
                elif(self.cardsInHand[i].type==self.cardsInHand[j].type):
                    if(self.cardsInHand[i].name<self.cardsInHand[j].name):
                        tmp=self.cardsInHand[i]
                        self.cardsInHand[i]=self.cardsInHand[j]
                        self.cardsInHand[j]=tmp
                        pass
    
    def playAgain(self):
        self.cardsInHand=[]
            
    def getCard(self,index):        
        return self.cardsInHand[index]

    def moveCard(self,index,x,y):
        self.cardsInHand[index].moveCard(x,y)
                
    def showCard(self,index,screen):
        background=self.getCardImg(index)
        screen.blit(background, (self.cardsInHand[index].rect))
        
    def moveAndShowCard(self,index,x,y,screen):
        self.moveCard(index, x, y)
        self.showCard(index, screen)

    def moveSlowly(self,index,x,y,screen):
        self.moveAndShowCard(index, x, y, screen)
        
    def refreshHand(self,screen):
        for i in range(0,13):
             if self.cardsInHand[i].isPlayed==False:
                 self.showCard(i, screen)
             elif self.currentPlay!=None :
                 if self.currentPlay.index==i:
                     self.showCard(i, screen)
                
                 
    def getForentCardImg(self,index):
        cardimg,cardrct=self.cardsInHand[index].getfrontImage()
        return cardimg
    
    def getCardImg(self,index):                
        
        cardimg,cardrct=self.cardsInHand[index].getfrontImage()
        return cardimg
        
        if self.isHuman==True :
            cardimg,cardrct=self.cardsInHand[index].getfrontImage()
        elif self.currentPlay!=None :
            if self.currentPlay.index==index :
                cardimg,cardrct=self.cardsInHand[index].getfrontImage()
            else:
                cardimg,cardrct=self.cardsInHand[index].getBackImage()
        else:
            cardimg,cardrct=self.cardsInHand[index].getBackImage()
        return cardimg
    
    def hastThisType(self,type):   
        for i in range(0,13):
            if self.cardsInHand[i].isPlayed==False:
                if self.cardsInHand[i].type==type:
                    return True
        return False

    def checkIsPlayHeart(self,playedCard):
        if self.isQueenSpadesPlayed==True and self.isPlayHeart==True :
            return 
        for i in range(0,len(playedCard)):
            for j in range(0,4):
                if playedCard[i][j].type==cardType.Hearts:
                    self.isPlayHeart=True
                if playedCard[i][j].type==cardType.Spades and  playedCard[i][j].name == cardNumber.queen :
                    self.isQueenSpadesPlayed=True
                if self.isQueenSpadesPlayed==True and self.isPlayHeart==True :
                    return 
    def checkPlayCard(self,cardToPlay,cardInGround,numOfDeckPlay):
        if(numOfDeckPlay==0):
            if len(cardInGround)==0:
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
        if len(cardInGround)==0:
            if(self.isPlayHeart==False  and cardToPlay.type==cardType.Hearts):
                self.errorMsg="You Can Not Play Hearts Now ! Take Another Card"
                return False
        else:
            if cardToPlay.type!=cardInGround[0][0].type:
                if self.hastThisType(cardInGround[0][0].type):
                    self.errorMsg="Check Your Card To Play,You Should Play Card As Type First Deck"
                    return False
        if(cardToPlay.type==cardType.Hearts) :     
            self.isPlayHeart=True


        self.errorMsg=None
        return True
     
        