
# If else

![image1](../../attachments/857d6b69ceec423a921ea19fbe20ea64.png)

![image2](../../attachments/d599f246099f45c8877dbe262cfb5f1c.png)

```
public class Main {
    public static void main(String[] args){
        int age = 16;
        if (age>=18) {
            System.out.println("adult : drive , vote");
        }
        else {
            System.out.println("not adult");
        }
    }
}


not adult
```


```
public class Main {
    public static void main(String[] args){
        int age = 16;
        if (age>=18) {
            System.out.println("adult : drive , vote");
        }

        if (age>=13 && age<18) {
            System.out.println("Teenager");
        }
        else {
            System.out.println("not adult");
        }
    }
}


Teenager
```

# Print the largest of 2 numbers 

```
public class Main {
    public static void main(String[] args){
        int A = 1;
        int B = 5;
        if (A>=B) {
            System.out.println("A is largest of 2");
        }
        else {
            System.out.println("B is largest of 2");
        }
    }
}


B is largest of 2
```

# Print if number is odd or even


![image7](../../attachments/8a566a8a041d49fe9e645488472decda.png)

![image8](../../attachments/fd374527bf8f4746b26fcc96401448ce.png)

# Else if 

If the first 'if' is true then the 'else if' statement will not be checked
Only if the first 'if' is false then 'else if' will be checked

![image9](../../attachments/7aeaeb80f71747349b4ec40db05db6dc.png)

![image10](../../attachments/c5840a5e190b47289cbb2d3c55b441c3.png)

![image11](../../attachments/f89e7a25eb834b84833f90d9b1902761.png)

![image12](../../attachments/4318f63d254b4dfea118776f5550a3f0.png)

![image13](../../attachments/cc1575b1d6a54dedb15aa1d595b3df77.png)

# Income Tax Calculator

![image14](../../attachments/f09a1c4f6fe84f65a6853a50cce2d044.png)

![image15](../../attachments/6b320070efc447b88c72c5b057879b82.png)

![image16](../../attachments/4fb475e4f811433ea0144067d0f76cc8.png)

# Print the largest of 3 numbers

![image17](../../attachments/c57110af5d21433a9738d7affe8973d2.png)

![image18](../../attachments/305e87cd881f43d2bbf87ead43c03b68.png)

![image19](../../attachments/470ca39451004f3fa80e5d9aea6963a3.png)

# Ternary operator

![image20](../../attachments/49f71348cf7e4d949b0ddc3d87076e03.png)

![image21](../../attachments/0aa3b3d1e3fd43b5926ae0025244bd86.png)

# Check if a student will Pass or Fail

![image22](../../attachments/51c4f956dabb43f8a04fe492ec7427b5.png)

![image23](../../attachments/e6e060543eb84854b55b0bb3f0c5156d.png)

# Switch statement 

![image24](../../attachments/b319532d24ff4e5d863a31784edc21e0.png)
It matches value after case to variable
Example , if value of variable is 2 , case 2 gets printed

![image25](../../attachments/eeada8bd3f8742f8a74fa3fbdadf1b45.png)
What is after the case matches the value of number
If the value is matched it prints what is written in the case

Also , also lines after the case gets printed if the case is matched

![image26](../../attachments/d0ac1270cad54111903f1c236ce8143f.png)
To print only the line of the matched case ,
Break ;
Is added after each line

![image27](../../attachments/0b58141436454abdbf1d717bf0d52119.png)
Characters can also be used instead of numbers
Or float values

# 
# Calculator

import java.util.Scanner;

public class Test {
public static void main(String\[\] args) {
Scanner sc = new Scanner(System.in);
System.out.println("enter a : ");
int a = sc.nextInt();
System.out.println("enter b : ");
int b = sc.nextInt();
System.out.println("enter operator : ");
char operator = sc.next().charAt(0);
switch (operator) {
case '+' : System.out.println(a+b);
break ;
case '-' : System.out.println(a-b);
break ;
case '\*' : System.out.println(a\*b);
break ;
case '/' : System.out.println(a/b);
break ;
case '%' : System.out.println(a%b);
break ;
default : System.out.println("wrong operator");
}
}
}

