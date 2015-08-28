Encrypting and Signing
==========================

It is critical to protect data from prying eyes and to assure that the data comes from a trusted sender. Hashes are often used to store passwords, but using the wrong hashing algorithm or choosing passwords that are too weak can still lead to problems. This exercise will teach you how to better protect data.

Learning Objectives
--------------------------
By the end of this lesson, you will be able to:

1. Encrypt a message.
2. Decrypt a message.
3. Sign a message.
4. Verify a digitally signed file.

Prerequisites
---------------------------
- Vagrant installed and configured
- A Windows Server 2012 virtual machine

Signing Files
------------------------------------
There are times when you want to sign a file so that people can verify who sent it. The GNU Privacy Guard application uses the industry standard PGP algorithm to sign and encrypt data.

### Create an Ubuntu Virtual Machine

Run the following commands in a new folder to create an Unbuntu virtual machine.
  - `> vagrant init ubuntu/trusty64`
  - `> vagrant up`
  - `> vagrant ssh`

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
