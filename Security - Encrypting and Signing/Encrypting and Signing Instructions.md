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
- A Windows Server 2012 virtual machine or a Windows computer

Signing Files
------------------------------------
There are times when you want to sign a file so that people can verify who sent it. The GNU Privacy Guard application uses the industry standard PGP algorithm to sign and encrypt data.

### Create an Ubuntu Virtual Machine

Run the following commands in a new folder to create an Unbuntu virtual machine.
1. `> vagrant init ubuntu/trusty64`
2. `> vagrant up`
3. `> vagrant ssh`

### Gnu Privacy Guard in Linux Installation and Key Creation

1. Run `$ sudo apt-get install rng-tools` to install random number generator tools.
2. Run `$ sudo rngd -r /dev/urandom` to generate enough random entropy to successfully generate a GPG key.
3. Run `$ gpg --gen-key` to start the key creation process.
  - Select (1) RSA and RSA (default)
  - Select 2048 bits
  - Select 0 so that the key does not expire, then y to confirm.
  - Enter your first name and a fake last name.
  - Enter a fake email address.
  - Leave the comment blank.
  - Press O for okay.
  - Enter a password, and repeat it when prompted.
4. Run `$ gpg --output /vagrant/namekey.asc --export -a 671DB6B1` but replace two elements. Replace 671DB6B1 with your key id. You can find in the output of the key creation on the line that says, "gpg: key 671DB6B1 marked as ultimately trusted." Also replace "name" with your first name.
  - This command outputs your public key. You can send this to others so that they can verify your signature.
5. Open [name]key.asc in your host operating system. The file will be in the same folder where you ran "vagrant init.""

### Clearsign Files with GnuPG in Linux

1. Run `$nano /vagrant/simple.txt`.
  - Add the text "This is very important."
  - Save the file using Control+O,[enter],Control+X.
2. Run `$ gpg --clearsign /vagrant/simple.txt`
  - Enter your password when prompted.
3. Open simple.txt.asc in a text editor.
  - Notice that you can read the text of the file, but that it is wrapped with a PGP signature.
  - If you send this file to somebody, that person could read the text without having to decrypt the file. They would also be able to verify that you were the person who sent it.

### Importing and Verifying Files in Linux

1. Rename your simple.txt file to "[name]simple.txt". Replace your name in the filename, and do not include brackets.
  - Send your [name]key.asc and [name]simple.txt.asc to a friend.
2. When you receive the files, copy them to your folder for this exercise.
3. Run the command `$ gpg --import /vagrant/[name]key.asc` to import their key.
4. Run the command `$ gpg --verify /vagrant/[name]simple.txt.asc` to verify the file.
  - Do you trust the signature?
  
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
