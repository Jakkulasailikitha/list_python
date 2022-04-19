from turtle import*
color ('black','blue')
begin_fill()
while True:
    forward(140)
    left(160)
    if abs(pos())<1:
        break
end_fill()
done()
