from file1 import MyFunc
import file1
from file1 import MyFunc as fn

MyFunc('Hi')
file1.MyFunc('Hello')
fn('Hello alias')