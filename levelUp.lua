-- Cargar la librería de UI
local Library = loadstring(game:HttpGet("https://raw.githubusercontent.com/xHeptc/Kavo-UI-Library/main/source.lua"))()
local Window = Library.CreateLib("AutoFarm - Age of Heroes", "BloodTheme")

local AutoFarmTab = Window:NewTab("AutoFarm")
local Section = AutoFarmTab:NewSection("Activados Automáticamente")

-- Variables
local player = game.Players.LocalPlayer
local rango = 15
getgenv().KillAura = true
getgenv().loopToCoordinates = true
getgenv().AntiKnockback = true

-- ✅ 1. Rapid Heavy Punch Kill Aura (sin escudo)
spawn(function()
	while KillAura do
		wait(0.005)
		pcall(function()
			local myHRP = player.Character and player.Character:FindFirstChild("HumanoidRootPart")
			if not myHRP then return end

			for _, v in pairs(game.Players:GetPlayers()) do
				if v ~= player and v.Character and v.Character:FindFirstChild("HumanoidRootPart") then
					local objetivoHRP = v.Character.HumanoidRootPart
					local distancia = (myHRP.Position - objetivoHRP.Position).Magnitude
					local tieneEscudo = v.Character:FindFirstChildOfClass("ForceField") or objetivoHRP:FindFirstChild("Shield") or v.Character:FindFirstChild("Shield")
					local estaVivo = v.Character:FindFirstChild("Humanoid") and v.Character.Humanoid.Health > 0

					if distancia < rango and not tieneEscudo and estaVivo then
						game:GetService("ReplicatedStorage").Events.Punch:FireServer(0.4, 0.1, 1)
					end
				end
			end
		end)
	end
end)

-- ✅ 2. Farm Zone #1 (TP loop a Edificio en construcción)
local function teleportLoop()
	while getgenv().loopToCoordinates do
		pcall(function()
			local character = player.Character or player.CharacterAdded:Wait()
			local rootPart = character:WaitForChild("HumanoidRootPart", 5)
			if rootPart then
				rootPart.CFrame = CFrame.new(650, 779, 284)
			end
		end)
		task.wait(2)
	end
end

spawn(teleportLoop)
player.CharacterAdded:Connect(function()
	if getgenv().loopToCoordinates then
		spawn(teleportLoop)
	end
end)

-- ✅ 3. Anti-Knockback
local LastPosition = nil
spawn(function()
	while getgenv().AntiKnockback do
		task.wait()
		local char = player.Character
		if char and char:FindFirstChild("HumanoidRootPart") then
			local part = char.HumanoidRootPart
			if part.AssemblyLinearVelocity.Magnitude > 250 or part.AssemblyAngularVelocity.Magnitude > 250 then
				part.AssemblyLinearVelocity = Vector3.new(0, 0, 0)
				part.AssemblyAngularVelocity = Vector3.new(0, 0, 0)
				if LastPosition then
					part.CFrame = LastPosition
				end
			elseif part.AssemblyLinearVelocity.Magnitude < 50 then
				LastPosition = part.CFrame
			end
		end
	end
end)

-- ✅ 4. No Clip (activar con tecla N)
local uis = game:GetService("UserInputService")
local noclip = false

uis.InputBegan:Connect(function(key)
	if key.KeyCode == Enum.KeyCode.N then
		noclip = not noclip
	end
end)

game:GetService("RunService").Stepped:Connect(function()
	if noclip then
		local char = player.Character
		if char then
			for _, v in pairs(char:GetDescendants()) do
				if v:IsA("BasePart") and v.CanCollide then
					v.CanCollide = false
				end
			end
		end
	end
end)

-- ✅ 5. Anti-AFK
for _, v in pairs(getconnections(game:GetService("Players").LocalPlayer.Idled)) do
	v:Disable()
end

game:GetService("Players").LocalPlayer.Idled:Connect(function()
	game:GetService("VirtualUser"):Button2Down(Vector2.new(0,0), workspace.CurrentCamera.CFrame)
	wait(1)
	game:GetService("VirtualUser"):Button2Up(Vector2.new(0,0), workspace.CurrentCamera.CFrame)
end)

Section:NewLabel("Script activo: Rapid Punch, FarmZone, AntiKnockback, NoClip, AntiAFK")
