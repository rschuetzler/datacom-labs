Hashing, Signing, and Encrypting
==========================

It is critical to protect data from prying eyes and to assure that the data comes from a trusted sender. 

Learning Objectives
--------------------------
By the end of this lesson, you will be able to:

1. Describe what hashing does.
2. Implement common hashing algorithms.
3. Encrypt a message.
4. Decrypt a message.
5. Sign a message.
6. Verify a digitally signed file.

Hashing
--------------------------

Cryptographic hash functions are algorithms that take data input and create a digest. The digest can be used to verify the contents of the file. The same hash algorithm can be run multiple times on the same file and will also return the same output. The digest length is typically fixed. A SHA-1 hash produces 20 byte digests no matter how large or small the input. A change in a single bit in a file will produce a radically different hash. It is impossible to reconstruct data from a given hash.

### Basic Hasing with CertUtil

Windoes comes preinstalled with CertUtil that can be used to hash files.

1. Create a file called "hashme.txt" in Windows Notepad.
2. Add the text, "This is a simple file" and save it. Use Notepad instead of other applications to avoid potential issues with character encoding.
3. In Windows Explorer, hold shift, and right-click on the folder containing hashme.txt. Select "Open a command prompt here."
4. In the command prompt, run `CertUtil -hashfile hashme.txt MD5`.
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
10. Run the following command to compute the hash digest using the SHA-1 algorithm: `CertUtil -hashfile hashme.txt SHA1`. You should see the following output.

SHA1 hash of file hashme.txt:
f7 1e 80 4b f7 49 30 9e 1f 32 b1 15 4c 67 88 2c d7 22 55 7e
CertUtil: -hashfile command completed successfully.

11. You can see that the SHA-1 digest is longer than the MD5 digest. SHA-1 is computationally more secure than MD5 and should be preferred.

Rainbow Tables
----------------------
Algorithms like MD5 and SHA-1 are suceptible to rainbow table attacks. Hash digests can be precomputed for shorter messages, like passwors. An attacker might be able to look up the hash in a database and find the value.

1. Go to https://crackstation.net/
2. Enter "09c9ea004b0c0822b75bdec322b90ff4" in the text box.
3. Enter the captcha if needed, then click "Crack Hashes."
4. You will see that the hash entered matches the MD5 hash for Waterfall.

Ideally, hashes could not be reverse engineered. But for short input, rainbow tables can be computed.

Salting
----------------------
Adds text to a message before the hash is computed. Developers can salt passwords as part of the password registration process to increase security, but this is an option left up to the reader.

Hashing with Bcrypt
--------------------------

Bcrypt is a good algorithm for hasing passwords. Bcrypt hashes change each time they are computed for a given password. But the hashes can still be verified.

1. Go to http://www.asecuritysite.com/encryption/bcrypt.
2. In the message, type "Hello".
3. Click "Generate Hash."
4. You will see a value similar to the following (but not the same)

```
Salt: $2a$06$A87nkZxS4bv0hGnpvgKUKO
Hash: $2a$06$A87nkZxS4bv0hGnpvgKUKOWgEOYcqtFF0S5GKaMiG9oVkoBji8mX2
```

5. Bcrypt generate salt automatically and computes a hash.
6. Click "Generate Hash" again. You should see different salt and hash values. For example:

```
Salt: $2a$06$nwFhaXe2e3dHMzd67t9Cs.
Hash: $2a$06$nwFhaXe2e3dHMzd67t9Cs.g0JLxmXhKG1KEb1QVameYklrIw30T1e
```

7. Go to https://www.dailycred.com/article/bcrypt-calculator and scroll down to Bcrypt Tester.
8. Enter "Hello" as the password and "$2a$06$A87nkZxS4bv0hGnpvgKUKOWgEOYcqtFF0S5GKaMiG9oVkoBji8mX2" as the hash then click Calculate.
9. You should see a message that the password and hash match.
10. Enter "Hello" as the password and "$2a$06$nwFhaXe2e3dHMzd67t9Cs.g0JLxmXhKG1KEb1QVameYklrIw30T1e" as the hash then click Calculate.
11. They should still match.
12. Enter "$2a$06$eINhL0/l0K6Y1LTSDubDieSANsrc2sDwxHP9vxihCl/P2o9KO9KcC" as the hash and click Calculate.
13. The password and the hash will NOT match.

Signing Files
------------------------------------
There are times when you want to sign a file so that people can verify who sent it. The GNU Privacy Guard application uses the industry standard PGP algorithm to sign and encrypt data.

### Installing GNU Privacy Guard and Creating a Key

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

### Sign a File

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

### Verifying a File

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


Encrypting Files
------------------------------------

1. Encrypte hashme.txt to create hashme.txt.gpg.
2. Open hashme.txt.gpg in a text editor to verify that the contents are unreadable.
3. Add yourself to the list of people this is being encrypted for.
4. Decrypt the file, entering your passphrase when prompted.