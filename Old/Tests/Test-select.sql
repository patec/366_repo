select * 
from user 
LEFT JOIN account ON account.uid = user.uid;
