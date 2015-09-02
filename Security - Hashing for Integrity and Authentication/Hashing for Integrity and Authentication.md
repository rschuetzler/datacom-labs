Hashing, Signing, and Encrypting
==========================

It is critical to protect data from prying eyes and to assure that the data comes from a trusted sender. Hashes are often used to store passwords, but using the wrong hashing algorithm or choosing passwords that are too weak can still lead to problems. This exercise will teach you how to better protect data.

Learning Objectives
--------------------------
By the end of this lesson, you will be able to:

1. Describe what hashing does.
2. Obtain the hash for files on Windows and Linux.
3. Encrypt a message.
4. Decrypt a message.
5. Sign a message.
6. Verify a digitally signed file.

Prerequisites
---------------------------
- Vagrant installed and configured
- A Windows Server 2012 virtual machine

Hashing
--------------------------

Cryptographic hash functions are algorithms that take data input and create a digest. The digest can be used to verify the contents of the file. The same hash algorithm can be run multiple times on the same file and will also return the same output. The digest length is typically fixed. A SHA-1 hash produces 20 byte digests no matter how large or small the input. A change in a single bit in a file will produce a radically different hash. It is impossible to reconstruct data from a given hash.

### Basic Hashing in Ubuntu

The default Ubuntu installation comes with tools to perform basic hashing.

1. In a new folder on your computer, run the following commands to bring up a new Unbuntu virtual machine.
  - `> vagrant init ubuntu/trusty64`
  - `> vagrant up`
  - `> vagrant ssh`
2. Run `$ cd /vagrant` to move folders. The /vagrant folder is synchronized with your host machine in the folder where you ran the `vagrant init` command. Any files you change within Ubuntu to these files will be changed on the host as well.
3. Run `$ nano simple.txt` to edit a text file.
4. Add the text "This is a simple file" (with no period at the end).
5. Save the file by pressing Control+o [enter], then Control+x to exit.
6. Run `$ sha1sum simple.txt` to calculate the hash. You should see the following output. Double check that you wrote the text exactly if your hash does not match.

```
76cfb6cad8170c70f014da2b201652911a4cff4d  simple.txt
```

7. Run `$ md5sum simple.txt` to calculate the hash using the MD5 algorithm. You should see the following output.

```
16f51623622aaa4faf5ab29abac970f6  simple.txt
```

8. Run `$ md5sum simple.txt` again. You should see the same hash value. SHA-1 and MD5 will produce the same result every time as long as the file contents do not change.

Note that the SHA-1 output is longer. SHA-1 procues a 160 bit hash, whereas MD5 produces a 128 bit hash. SHA-1 is stronger not only because the hash is longer, but because it is more difficult to crack.


Rainbow Tables
----------------------
Algorithms like MD5 and SHA-1 are suceptible to rainbow table attacks. Hash digests can be precomputed for shorter messages, like passwors. An attacker might be able to look up the hash in a database and find the value.

1. Go to https://crackstation.net/
2. Enter "09c9ea004b0c0822b75bdec322b90ff4" in the text box.
3. Enter the captcha if needed, then click "Crack Hashes."
4. You will see that the hash entered matches a common word with a capital letter.

Ideally, hashes could not be reverse engineered. But for short input, rainbow tables can be computed.

Salting
----------------------
Adds text to a message before the hash is computed. If hashing passwords with MD5 or SHA-1, developers can add some text to the users' passwords before hashing them. When verifying the hash (such as during a login), developers would add the salt to the users' input before verifying the hash. For example, a person might choose the password `jedi`. It would be an easy password to crack because Star Wars related terms are in most password cracking dictionaries. But to protect passwords, the developer might hash the password `myappjedi`. When the user logs in, he would input the password `jedi`, but the developer would test for a password match by hashing `myappjedi`. In an ideal world, the salt used would be kept secret so that attackers would not know how to create a custom rainbow table using the salt. If the salt is kept in the program source code or configuration files, the salt would be safe in the event where an attacker gained access to data but no application files. A downside to traditional salting methods is that developers must choose to implement them. 

Hashing with PBKDF2
--------------------------
Password-Based Key Derivation Function 2 (PBKDF2) and bcrypt usekey stretching to avoid brute force attacks. Wi-Fi Protected Access II (WPA2) and several operating systems use PBKDF2 to store passwords.

1. Run `$ grub-mkpasswd-pbkdf2`.
2. Enter the password `secure` when prompted.
3. Re-enter the password when prompted.
4. You should see output similar to the following:

```
PBKDF2 hash of your password is grub.pbkdf2.sha512.10000.33A3669C79BBA1036E78CF2
C8F459B86BC4A96C16FAA9A1CDE666914D5BD354532E6604B3E3297D37BA2C328BEE03CC9C960F3B
D15A805141CA57B7478BDFCDE.9157F0B21961B5785F50649C06E5B1B6B0F4C430DB77E589FA4FB3
47614781C073D94F17029EAAC848667C4327CBB7CC74C39F4EC0653E95C7E1E5017B575F9F
```

5. Run `$ grub-mkpasswd-pbkdf2` again.
6. Enter the same password as before, and confirm it when prompted.
7. Notice that the same password has a different PBKDF2 hash.

```
PBKDF2 hash of your password is grub.pbkdf2.sha512.10000.D35FFA8CC1C2A08A4971399
C63C8BB2B50F50C07B03ACA6D98A13B453EDCA468DBF023E00765862A465C31DD65A3C93A51FDF4E
5363BD1CC512C1318D5FFC654.67595812F2C9B94FC482FAA6C120FB7278D47B2EF51A38D1BA0140
2037A52FC523ECEDF4FD8EE2CA12ED83A15AA6FE757D2BD95EF1D98E7928BC9AE11E5F7ED4
```

Hashing with Bcrypt
--------------------------

Bcrypt is a good algorithm for storing passwords securely. Bcrypt hashes change each time they are computed for a given password. But the hashes can still be verified. Bcrypt is great for passwords, but MD5 or SHA-1 are better choices for hasing large files.

1. Go to http://www.asecuritysite.com/encryption/bcrypt.
2. In the message, type "Hello".
3. Click "Generate Hash."
4. You will see a value similar to the following (but not the same)

```
Salt: $2a$06$A87nkZxS4bv0hGnpvgKUKO
Hash: $2a$06$A87nkZxS4bv0hGnpvgKUKOWgEOYcqtFF0S5GKaMiG9oVkoBji8mX2
```

5. Bcrypt generates salt automatically and computes a hash.
6. Click "Generate Hash" again. You should see different salt and hash values. For example:

```
Salt: $2a$06$nwFhaXe2e3dHMzd67t9Cs.
Hash: $2a$06$nwFhaXe2e3dHMzd67t9Cs.g0JLxmXhKG1KEb1QVameYklrIw30T1e
```

7. Go to https://www.dailycred.com/article/bcrypt-calculator and scroll down to Bcrypt Tester.
8. Enter "Hello" as the password.
  - Enter the following hash:
  
```
$2a$06$A87nkZxS4bv0hGnpvgKUKOWgEOYcqtFF0S5GKaMiG9oVkoBji8mX2
```

  - Click click Calculate.
9. You should see a message that the password and hash match.
10. Enter "Hello" as the password.
  - Enter the following hash

```
$2a$06$nwFhaXe2e3dHMzd67t9Cs.g0JLxmXhKG1KEb1QVameYklrIw30T1e
```

  - Click Calculate.
11. They should still match.
12. Enter the following hash:

```
$2a$06$eINhL0/l0K6Y1LTSDubDieSANsrc2sDwxHP9vxihCl/P2o9KO9KcC
```

  - Click Calculate.

13. The password and the hash will NOT match.

Hashing for Integrity and Authentication with HMAC
---------------------------------------------------

Run the following commands in your Linux virtual machine.

1. Run `$ echo -n "This is my message" | openssl dgst -sha1 -hmac "secretkey"`.
  - The `echo` command outputs text to the console.
  - The `-n` flag tells the echo command not to put a newline at the end of the message.
  - The part in quotes tells echo what to output.
  - The "|" redirects (pipes) the output of the echo command into the following openssl command.
  - `openssl` us a cryptography toolkit that can create HMAC digests.
2. You should see the following output.

```
(stdin)= 2e79892fcc2cb8842c1fca6872b84b7173971bac
```

3. Run the command again. Verify that the output is unchanged.

Signing Files
------------------------------------
There are times when you want to sign a file so that people can verify who sent it. The GNU Privacy Guard application uses the industry standard PGP algorithm to sign and encrypt data.

### Gnu Privacy Guard in Linux Installation and Key Creation

1. Run `$ sudo apt-get install gpg` to install the Gnu Privacy Guard.
2. Run `$ sudo apt-get install rng-tools` to install random number generator tools.
3. Run `$ sudo rngd -r /dev/urandom` to generate enough random entropy to successfully generate a GPG key.
4. Run `$ gpg --gen-key` to start the key creation process.
  - Select (1) RSA and RSA (default)
  - Select 2048 bits
  - Select 0 so that the key does not expire, then y to confirm.
  - Enter your first name and a fake last name.
  - Enter a fake email address.
  - Leave the comment blank.
  - Press O for okay.
  - Enter a password, and repeat it when prompted.
5. Run `$ gpg --output namekey.asc --export -a 671DB6B1` but replace two elements. Replace 671DB6B1 with your key id. You can find in the output of the key creation on the line that says, "gpg: key 671DB6B1 marked as ultimately trusted." Also replace "name" with your name.
  - This command outputs your public key. You can send this to others so that they can verify your signature.

### Clearsign Files with GnuPG in Linux

1. Run `$ gpg --clearsign simple.txt`
2. Open simple.txt.asc in a text editor.
  - Notice that you can read the text of the file, but that it is wrapped with a PGP signature.
  - If you send this file to somebody, that person could read the text without having to decrypt the file. They would also be able to verify that you were the person who sent it.

Hashing on Windows
------------------------------------

### Windows Hashing with CertUtil

Windows comes preinstalled with CertUtil that can be used to hash files. Run the following section in a Windows 2012 Server virtual machine.

1. Open PowerShell.
2. Navigate to the desktop folder by running `cd desktop`.
3. Run `> notepad hashme.txt` to start notepad.
  - You will get a message indicating that hashme.txt is not found. Click"yes" to create the file.
4. Add the text, "This is a simple file" and save it. Use Notepad instead of other applications to avoid potential issues with character encoding.
5. In PowerShell command prompt, run `> CertUtil -hashfile hashme.txt MD5`.
5. You should see the following output.

```
MD5 hash of file hashme.txt:
19 0a a3 11 7b 11 aa b3 f2 c5 f4 e5 f7 d9 e4 02
CertUtil: -hashfile command completed successfully.
```

6. The output is in hexadecimal format, with values from 0 to 16 represented by 0-9a-f. You hash should match as long as you typed the message exactly.
7. Change hashme.txt to add a period at the end of the sentence.
8. Re-run the MD5 hash. You should see the following output.

```
MD5 hash of file hashme.txt:
41 02 45 8b d1 69 b0 99 8c 01 97 ee cb 3c 2d f3
CertUtil: -hashfile command completed successfully.
```

9. The hash is completely different from before. If you gave somebody the hash, they would have no idea what the original file was.
10. Run the following command to compute the hash digest using the SHA-1 algorithm: `> CertUtil -hashfile hashme.txt SHA1`. You should see the following output.

SHA1 hash of file hashme.txt:
f7 1e 80 4b f7 49 30 9e 1f 32 b1 15 4c 67 88 2c d7 22 55 7e
CertUtil: -hashfile command completed successfully.

11. You can see that the SHA-1 digest is longer than the MD5 digest. SHA-1 is computationally more secure than MD5 and should be preferred.

  
Gnu Privacy Guard on Windows
------------------------------------
  
### Installing GNU Privacy Guard on Windows and Creating a Key

1. Go to http://gpg4win.org/download.html and download the GNU Privacy Guard.
2. Find the download link for Gpg4win. Download and install the full version. Accept the default installatin options.
3. Run the newly installed program Kleopatra found in the Gpg4win folder in the start menu.
4. Click File > New Certificate.
5. Choose "Create a personal OpenPGP key pair."
6. Enter your name and email, then click Next.
7. Click "Create Key."
8. Enter the passphrase "signer". You will be warned that the passphrase is weak (which is true), but select the option to continue with the weak passphrase.
9. Re-enter the passphrase when prompted.
10. You will see a success message with a key fingerprint.

```
Certificate created successfully.
Fingerprint: BD94A43C05E30F42CE1E9FFA8959E4FF4531D8AD
```

11. The key fingerprint can be shared publicly. Anybody can verify that they have the correct public key by checking the fingerprint.
12. Click Finish.

### Windows: Sign a File with GnuPG

1. In Kleopatra, click File > Sign/Encrypt Files...
2. Find hashme.txt
3. Select "Sign" only.
4. Check "Text output (ASCII armor)" so that the result is more readable.
5. Keep the other default options.
6. Enter the passphrase when prompted (signer).
7. Open the generated file hashme.txt.asc in a text editor.
8. With your public certificate, others could now verify this signature.
9. In the Kleopatra main window, select your certificate. Click the "Export Certificates" button. Choose a friendlier name, such as yourname.asc.
10. Send your certificate and the signed file (hashme.txt.asc) to a classmate.
11. When you receive a certificate from a classmate, import the certificate using the "Import Certificates" function.

### Windows: Verifying a File with GnuPG

1. Click Settings > Configure Kleopatra.
2. With "Directory Services" highlighted, click the down arrow next to "New" and select OpenPGP and click OK.
3. The download page http://gpg4win.org/download.html  lists a Key-ID that was used to sign the executables.
4. In Keopata, click "Lookup certificates on server" and search for that key ID, adding "0x" to the beginning, e.g. 0xEC70B1B8.
5. When you find the certificate, import it.
6. Right-click on the imported certificate and choose "Certify Certificate."
7. Check both boxes and click Next, Certify, and enter your passphrase (signer) when prompted.
8. Click File > Decrypt/Verify files.
9. Select the Gpg4win installation executable and click OK.

### Bonus

Check the hash on the installation file to determine if the hash matches the value publishe don the website.


Windows: Encrypting Files with GnuPG
------------------------------------

1. Encrypt hashme.txt to create hashme.txt.gpg.
2. Open hashme.txt.gpg in a text editor to verify that the contents are unreadable.
3. Add yourself to the list of people this is being encrypted for.
4. Decrypt the file, entering your passphrase when prompted.
