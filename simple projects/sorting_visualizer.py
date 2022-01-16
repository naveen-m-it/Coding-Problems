
import time
import pygame
import random
WIDTH=500
WIN=pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Sorting visualizer")
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
YELLOW = (255,255,0)
BLACK = (0,0,0)
class Spot:
    def __init__(self,row,col,width,total_rows) -> None:
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = WHITE
        self.total_rows = total_rows
        self.width = width
def mergeSort(win,arr):
    x = WIDTH//len(arr)
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(win,L)
        mergeSort(win,R)
        i=j=k=0
        while i<len(L) and j<len(R):
            pygame.draw.rect(win,WHITE,((arr[i]-1)*x,0,x-1,x*arr[i]))
            pygame.display.update()
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
def partition(win,arr,start,end):
    x = WIDTH//len(arr)
    pivot = arr[start]
    low = start+1
    high = end
    while True:
        pygame.draw.rect(win,WHITE,((low)*x,0,x-1,x*arr[low]))
        pygame.draw.rect(win,GREEN,((high)*x,0,x-1,x*arr[high]))
        pygame.display.update()
        while low<=high and arr[high]>=pivot:
            high = high-1
        while low<=high and arr[low]<=pivot:
            low = low+1
        if low<=high:
            arr[low],arr[high] = arr[high],arr[low]
            pygame.draw.rect(win,RED,((high)*x,0,x-1,x*arr[high]))
            pygame.draw.rect(win,YELLOW,((low)*x,0,x-1,x*arr[low]))
            pygame.display.update()
        else:
            break
    arr[start],arr[high] = arr[high],arr[start]
    pygame.draw.rect(win,BLUE,((start)*x,0,x-1,x*arr[start]))
    pygame.draw.rect(win,BLACK,((high)*x,0,x-1,x*arr[high]))
    pygame.display.update()
    return high
def quickSort(win,arr,low,high):
    x = WIDTH//len(arr)
    if low>=high:
        return
    p = partition(win,arr,low,high)
    quickSort(win,arr,low,p-1)
    quickSort(win,arr,p+1,high)
    for i in range(len(arr)):
        pygame.draw.rect(win,WHITE,((i)*x,0,x-1,x*arr[i]))
        pygame.display.update()
        pygame.draw.rect(win,BLUE,((i)*x,0,x-1,x*arr[i]))
        pygame.display.update()

def insertionSort(win,arr):
    x = WIDTH//len(arr)
    for i in range(len(arr)):
        min_ind = i
        for j in range(i+1,len(arr)):
            pygame.draw.rect(win,RED,((j)*x,0,x-1,x*arr[j]))
            pygame.draw.rect(win,WHITE,((min_ind)*x,0,x-1,x*arr[min_ind]))
            pygame.display.update()
            if arr[min_ind]>arr[j]:
                min_ind = j
        arr[i],arr[min_ind] = arr[min_ind],arr[i]
        pygame.draw.rect(win,BLACK,((i)*x,0,x-1,x*arr[i]))
        pygame.draw.rect(win,BLUE,((min_ind)*x,0,x-1,x*arr[min_ind]))
        pygame.display.update()
        time.sleep(.01)
    for i in range(len(arr)):
        pygame.draw.rect(win,BLACK,((i)*x,0,x-1,x*arr[i]))
        pygame.display.update()
        time.sleep(.001)
        pygame.draw.rect(win,BLUE,((i)*x,0,x-1,x*arr[i]))
        pygame.display.update()
    
def bubbleSort(win,arr):
    x = WIDTH//len(arr)
    for i in range(len(arr)):
        already = True
        for j in range(len(arr)-i-1):
            pygame.draw.rect(win,WHITE,((j)*x,0,x-1,x*arr[j]))
            pygame.draw.rect(win,GREEN,((j+1)*x,0,x-1,x*arr[j+1]))
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                pygame.draw.rect(win,RED,((j+1)*x,0,x-1,x*arr[j+1]))
                pygame.draw.rect(win,YELLOW,((j)*x,0,x-1,x*arr[j]))
                already = False
                pygame.display.update()
            pygame.draw.rect(win,BLUE,((j)*x,0,x-1,x*arr[j]))
            pygame.draw.rect(win,BLACK,((j+1)*x,0,x-1,x*arr[j+1]))
            pygame.display.update()
        if already:
            break
    for i in range(len(arr)):
        pygame.draw.rect(win,GREEN,((i)*x,0,x-1,x*arr[i]))
        pygame.display.update()
        pygame.draw.rect(win,BLUE,((i)*x,0,x-1,x*arr[i]))
        pygame.display.update()
def main(win):
    win.fill(WHITE)
    arr = [x for x in range(1,51)]
    x = WIDTH//len(arr)
    random.shuffle(arr)
    for i in range(len(arr)):
        pygame.draw.rect(win,BLUE,((i)*x,0,x-1,x*arr[i]))
        pygame.display.update()
        time.sleep(.01)
    bubbleSort(win,arr)
    print(arr)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()
main(WIN)
