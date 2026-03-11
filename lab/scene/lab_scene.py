"""3D lab scene generator using browser-side Three.js."""

from __future__ import annotations


def build_lab_scene_html() -> str:
    return """
    <div id='lab3d' style='width:100%;height:520px;background:#0f1117;border:1px solid #2a2f3a;border-radius:8px;'></div>
    <script type='module'>
      import * as THREE from 'https://unpkg.com/three@0.160.0/build/three.module.js';
      import { OrbitControls } from 'https://unpkg.com/three@0.160.0/examples/jsm/controls/OrbitControls.js';
      const container = document.getElementById('lab3d');
      const scene = new THREE.Scene();
      scene.background = new THREE.Color(0x0f1117);

      const camera = new THREE.PerspectiveCamera(55, container.clientWidth/container.clientHeight, 0.1, 100);
      camera.position.set(6, 4, 8);

      const renderer = new THREE.WebGLRenderer({antialias:true});
      renderer.setSize(container.clientWidth, container.clientHeight);
      renderer.setPixelRatio(window.devicePixelRatio);
      container.appendChild(renderer.domElement);

      const controls = new OrbitControls(camera, renderer.domElement);
      controls.target.set(0, 1, 0);
      controls.update();

      const hemi = new THREE.HemisphereLight(0xdde8ff, 0x10141d, 0.9);
      scene.add(hemi);
      const dir = new THREE.DirectionalLight(0xffffff, 0.8);
      dir.position.set(5, 8, 2);
      scene.add(dir);

      const floor = new THREE.Mesh(new THREE.PlaneGeometry(20,20), new THREE.MeshStandardMaterial({color:0x1a1f2b, roughness:0.95}));
      floor.rotation.x = -Math.PI/2;
      scene.add(floor);

      function bench(x, z, color=0x394255) {
        const mesh = new THREE.Mesh(new THREE.BoxGeometry(2.8, 1.0, 1.2), new THREE.MeshStandardMaterial({color}));
        mesh.position.set(x, 0.5, z);
        scene.add(mesh);
        const panel = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.4, 0.08), new THREE.MeshStandardMaterial({color:0x7ec8ff, emissive:0x163145}));
        panel.position.set(x, 1.1, z+0.55);
        scene.add(panel);
      }

      bench(-2.8, -1.8);
      bench(0.0, -1.8, 0x4f5c74);
      bench(2.8, -1.8);

      const rack = new THREE.Mesh(new THREE.BoxGeometry(1.2, 3.2, 0.6), new THREE.MeshStandardMaterial({color:0x2b3344}));
      rack.position.set(4.4, 1.6, 1.8);
      scene.add(rack);

      const cablePath = new THREE.BufferGeometry().setFromPoints([
        new THREE.Vector3(-3.8,0.05,-1.2), new THREE.Vector3(-1.5,0.05,-0.8), new THREE.Vector3(0.4,0.05,-1.1), new THREE.Vector3(2.9,0.05,-1.4)
      ]);
      const cable = new THREE.Line(cablePath, new THREE.LineBasicMaterial({color:0xff8f6b}));
      scene.add(cable);

      function animate(){ requestAnimationFrame(animate); renderer.render(scene,camera); }
      animate();

      window.addEventListener('resize', () => {
        camera.aspect = container.clientWidth/container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
      });
    </script>
    """
