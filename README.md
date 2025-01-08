**steps to remove a repository (saving this shit bc im forgetful)**

**1. clone repository**

     
        git clone https://github.com/maicaalmonte/maicaalmonte.git
        cd maicaalmonte

**2. view commit history**

    
        git log

**3. reset or rebase**
<br>a.  reset your current branch to a specific commit

     
        git reset --hard 27884ee50b6abfb209b33feef3edd89d1e14c0d2^

b. interactive rebase to modify commits in your history:
    
    
        git rebase -i 27884ee50b6abfb209b33feef3edd89d1e14c0d2^
    


**4. to remove the commit you want to remove in the list of commits**
<br>a. look for the line corresponding to the commit

    
        pick 27884ee <commit message>
 <br>b. change the word pick to drop

     
         drop 27884ee <commit message>

  **5. save the file and exit**

    
        press "ESC", type "wq", and press "ENTER"

**6. force push to github**

    
        git push origin main --force

#
**OTHERS**

<br> 1. check current path in powershell

    
        echo $env:PATH

<br>2. configuration file PostgreSQL:

     notepad "C:\Program Files\PostgreSQL\17\data\postgresql.conf"

    


