#include <stdio.h>

// ---------------- FCFS ----------------
void fcfs(int n, int bt[], float *avg_wt, float *avg_tat) {
    int wt[n], tat[n];

    wt[0] = 0;
    for (int i = 1; i < n; i++)
        wt[i] = wt[i-1] + bt[i-1];

    for (int i = 0; i < n; i++)
        tat[i] = wt[i] + bt[i];

    float total_wt = 0, total_tat = 0;

    printf("\n--- FCFS ---\n");
    for (int i = 0; i < n; i++) {
        printf("P%d -> WT=%d , TAT=%d\n", i+1, wt[i], tat[i]);
        total_wt += wt[i];
        total_tat += tat[i];
    }

    *avg_wt = total_wt / n;
    *avg_tat = total_tat / n;

    printf("Average WT = %.2f\n", *avg_wt);
    printf("Average TAT = %.2f\n", *avg_tat);
}

// ---------------- SJF ----------------
void sjf(int n, int bt[], float *avg_wt, float *avg_tat) {
    int wt[n], tat[n], temp;

    // copy array عشان منبوظش الأصل
    int b[n];
    for (int i = 0; i < n; i++) b[i] = bt[i];

    // sort
    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {
            if (b[i] > b[j]) {
                temp = b[i];
                b[i] = b[j];
                b[j] = temp;
            }
        }
    }

    wt[0] = 0;
    for (int i = 1; i < n; i++)
        wt[i] = wt[i-1] + b[i-1];

    for (int i = 0; i < n; i++)
        tat[i] = wt[i] + b[i];

    float total_wt = 0, total_tat = 0;

    printf("\n--- SJF ---\n");
    for (int i = 0; i < n; i++) {
        printf("P%d -> WT=%d , TAT=%d\n", i+1, wt[i], tat[i]);
        total_wt += wt[i];
        total_tat += tat[i];
    }

    *avg_wt = total_wt / n;
    *avg_tat = total_tat / n;

    printf("Average WT = %.2f\n", *avg_wt);
    printf("Average TAT = %.2f\n", *avg_tat);
}

// ---------------- Round Robin ----------------
void rr(int n, int bt[], int tq, float *avg_wt, float *avg_tat) {
    int rt[n], wt[n], tat[n];

    for (int i = 0; i < n; i++) {
        rt[i] = bt[i];
        wt[i] = 0;
    }

    int time = 0;

    while (1) {
        int done = 1;

        for (int i = 0; i < n; i++) {
            if (rt[i] > 0) {
                done = 0;

                if (rt[i] > tq) {
                    time += tq;
                    rt[i] -= tq;
                } else {
                    time += rt[i];
                    wt[i] = time - bt[i];
                    rt[i] = 0;
                }
            }
        }

        if (done) break;
    }

    float total_wt = 0, total_tat = 0;

    printf("\n--- Round Robin ---\n");
    for (int i = 0; i < n; i++) {
        tat[i] = wt[i] + bt[i];
        printf("P%d -> WT=%d , TAT=%d\n", i+1, wt[i], tat[i]);
        total_wt += wt[i];
        total_tat += tat[i];
    }

    *avg_wt = total_wt / n;
    *avg_tat = total_tat / n;

    printf("Average WT = %.2f\n", *avg_wt);
    printf("Average TAT = %.2f\n", *avg_tat);
}

// ---------------- MAIN ----------------
int main() {
    int n, choice, tq;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    int bt[n];

    for (int i = 0; i < n; i++) {
        printf("Enter Burst Time for P%d: ", i+1);
        scanf("%d", &bt[i]);
    }

    printf("\n1. FCFS\n2. SJF\n3. Round Robin\n4. Compare All\n");
    printf("Choose: ");
    scanf("%d", &choice);

    float avg_wt1, avg_tat1;
    float avg_wt2, avg_tat2;
    float avg_wt3, avg_tat3;

    switch(choice) {
        case 1:
            fcfs(n, bt, &avg_wt1, &avg_tat1);
            break;

        case 2:
            sjf(n, bt, &avg_wt2, &avg_tat2);
            break;

        case 3:
            printf("Enter Time Quantum: ");
            scanf("%d", &tq);
            rr(n, bt, tq, &avg_wt3, &avg_tat3);
            break;

        case 4:
            printf("Enter Time Quantum for RR: ");
            scanf("%d", &tq);

            fcfs(n, bt, &avg_wt1, &avg_tat1);
            sjf(n, bt, &avg_wt2, &avg_tat2);
            rr(n, bt, tq, &avg_wt3, &avg_tat3);

            printf("\n--- Comparison ---\n");
            printf("Algorithm     Avg WT     Avg TAT\n");
            printf("--------------------------------\n");
            printf("FCFS          %.2f      %.2f\n", avg_wt1, avg_tat1);
            printf("SJF           %.2f      %.2f\n", avg_wt2, avg_tat2);
            printf("RR            %.2f      %.2f\n", avg_wt3, avg_tat3);
            break;

        default:
            printf("Invalid choice\n");
    }

    return 0;
}
