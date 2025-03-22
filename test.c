// scanf("%d",&n);
// for(int i=0;i<=n;i++)
// {
//     for(int j=0;j<i;j++)
//     {
//         // O(1) kisu akta kaj
//     }
// }
// 0 + 1 + 2 + 3 +.....+(n-1)+ n
// = n(n+1)/2 = n**2/2 + n/2
// = O(n**2)

// scanf("%d",&n);
// p = 0
// for(int i=0;p < n;i++)
// {
//     // kisu akta kaj= O(1)= o(k)
//     p+=i
// }
// i       p
// 0       0
// 1       1
// 2       1+2
// 3       1+2+3
// .       .
// .       .
// k       1+2+3+....+(k-1) +k = k(k+1)/2

// p=n
// k(k+1)/2 = n
// // for worst case k**2 = n
// o(k)= O(✓n)

// scanf("%d", &n);
// for (int i = 1; i < n; i*=2)
// //1 2 4 8 16 32
// {
//     // kisu akta kaj O(1) = k = log2n
// }
// O(k)
// {i}
// 2**0=1
// 2**1
// 2**2
// 2**3
// 2**4
// .
// .
// 2**k ; i=n
// 2**k = n
// // k = log2(n)

// scanf("%d",&n);
// for(int i=0; i*i< n ;i+=1)
// {

// }
// i*i = n
// i = ✓n
// O(✓n)

// i-----n O(n)
// i-----n/2 O(n)
// i-----✓n---O(✓n)

// i=n
// while(i>=1)
// {
//     i/=2
// }

// i=1 .2.4.8.. n
// {
//     scanf("%d",&n);
//     for (int i = 0; i < n - 100; i += 99)
//     {
//         pass
//     }
//     {(n-100)/99}
// }

// scanf("%d",&n);
// for(int i=0;i<n-10000;i+=1)
// {
//     pass
// }
// n=16
// {
//     p = 0 
//     for(int i=1;i<n;i*=2)
//     {
//         p+=1 ------ p = log2(n)
//     }
//     for(int j=1;j<p;j*=2)
//     {
//         // kisu akta jar compx O(1) -- log2(p)
//     }

// } 


// for(int i=0;i<n;i++)
// {
//     for(int j=1;j<n;j*=2)
//     {
//         O(n)
//     }
// }

// n*log(n)

// int n;
// 2**31-1 
// scanf("%d",&n);

// for(int i=0;i<n;i++)
// {
//     printf("*");
// }