class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int m = image.size(), n = image[0].size();
        dfs(image, sr, sc, m, n, image[sr][sc], color);
        return image;
    }
    void dfs(vector<vector<int>>& image, int r, int c, int m, int n,int target, int newColor){
        if (r < 0 || c < 0 || r >= m || c >= n || image[r][c] != target || image[r][c] == newColor) return;
        image[r][c] = newColor;
        dfs(image, r-1, c, m, n, target, newColor);
        dfs(image, r+1, c, m, n, target, newColor);
        dfs(image, r, c-1, m, n, target, newColor);
        dfs(image, r, c+1, m, n, target, newColor);
    }
};