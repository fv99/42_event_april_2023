#include <stdio.h>
#include <string.h>

int max_length(int argc, char **argv) {
    int max_len = 0;
    for (int i = 1; i < argc; ++i) {
        int len = strlen(argv[i]);
        if (len > max_len) {
            max_len = len;
        }
    }
    return max_len;
}

void print_frame_line(int length) {
    for (int i = 0; i < length; ++i) {
        putchar('*');
    }
    putchar('\n');
}

int main(int argc, char **argv) {
    if (argc == 1) {
        return 0;
    }

    int max_len = max_length(argc, argv);
    int frame_width = max_len + 4;

    print_frame_line(frame_width);

    for (int i = 1; i < argc; ++i) {
        int padding = max_len - strlen(argv[i]);
        printf("* %s", argv[i]);
        for (int j = 0; j < padding; ++j) {
            putchar(' ');
        }
        printf(" *\n");
    }

    print_frame_line(frame_width);

    return 0;
}
