#include <stdio.h>



int i, n, a, b, cnt;

int *m;



int main(void)

{

  while(scanf("%d",&n) == 1)

  {

    m = new int[n];

    for(i = 0; i < n; i++)

      scanf("%d",&m[i]);

    scanf("%d %d",&a,&b);

    for(cnt = i = 0; i < n; i++)

      if ((m[i] >= a) && (m[i] <= b)) cnt++;

    printf("%d\n",cnt);

    delete [] m;

  }

  return 0;

}
