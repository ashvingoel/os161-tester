/*
 * sty.c
 *
 * 	Run a bunch of cpu pigs.
 *
 * This test should itself run correctly when the basic system calls
 * are complete. It may be helpful for scheduler performance analysis.
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <err.h>

static char *hargv[2] = { (char *)"hog", NULL };

#define MAXPROCS        9
#define DEFAULTPROCS    6

static int pids[MAXPROCS], npids;

static
void
hog(void)
{
	int pid = fork();
	switch (pid) {
	    case -1:
		err(1, "fork");
	    case 0:
		/* child */
		execv("/testbin/hog", hargv);
		err(1, "/testbin/hog");
	    default:
		/* parent */
		pids[npids++] = pid;
		break;
	}
}

static
int
waitall(void)
{
	int i, status, n = 0;
	for (i=0; i<npids; i++) {
		if (waitpid(pids[i], &status, 0)<0) {
			warn("waitpid for %d", pids[i]);
		}
		else if (status != 0) {
			warnx("pid %d: exit %d", pids[i], status);
		}
		else {
		    n++;
		}
	}
	
	return n;
}

static
void 
usage(void)
{
    printf("usage: sty [NUM]\n"
           "  NUM: must be from 1 to 9 inclusive\n");
    exit(1);
}

int
main(int argc, const char *argv[])
{
    int nhogs = DEFAULTPROCS;
    
    if ( argc == 2 ) {
        int tmp = atoi(argv[1]);
        if ( tmp <= 0 || tmp > MAXPROCS ) {
            usage();
        }
        nhogs = tmp;
    } 
    else if ( argc > 2 ) {
        usage();
    }

    while ( nhogs > 0 ) {
	    hog();
	    nhogs--;
	}
	nhogs = waitall();
	
	if ( nhogs == 0 ) {
	    printf("who let the hogs out?!\n");
	} else if ( nhogs == 1 ) {
	    printf("one lonely hog went back in the pen.\n");
	} else {
	    printf("%d hogs are back in the pen.\n", nhogs);
	}
	
	return 0;
}
