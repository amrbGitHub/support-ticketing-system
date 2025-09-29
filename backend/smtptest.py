import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587) # start smtp server will TLS port
server.starttls() # start server with TLS 
# Login to gmail account
# password : apln uumy etdw bodj 
server.login('amrstestemail4dev@gmail.com', 'apln uumy etdw bodj')
