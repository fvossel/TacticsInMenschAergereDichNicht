import { defineConfig } from "vite";
import { viteSingleFile } from "vite-plugin-singlefile";

// D-43: the build target is a single self-contained HTML file with all JS and
// CSS inlined. A default Vite build emits <script type="module">, which
// browsers refuse to load over file:// (opaque origin, CORS-governed module
// loading) -- the shell would render blank, contradicting UI-2's promise that
// the viewer runs offline from disk. AK-6 opens the built artifact directly.
export default defineConfig({
  plugins: [viteSingleFile()],
  build: {
    target: "es2022",
    assetsInlineLimit: 100_000_000,
    chunkSizeWarningLimit: 100_000,
    cssCodeSplit: false,
    rollupOptions: { output: { inlineDynamicImports: true } },
  },
});
