scoreboard objectives add ONE_SECOND dummy "ONE_SECOND"
scoreboard players set ONE_SECOND ONE_SECOND 20

scoreboard objectives add WAIT_SECONDS dummy "WAIT_SECONDS"
scoreboard players set WAIT_SECONDS WAIT_SECONDS 10

scoreboard objectives add WAIT_TICKS dummy "WAIT_TICKS"
scoreboard players operation WAIT_TICKS WAIT_TICKS = ONE_SECOND ONE_SECOND
scoreboard players operation WAIT_TICKS WAIT_TICKS *= WAIT_SECONDS WAIT_SECONDS

scoreboard objectives add START_TIME dummy "START_TIME"
scoreboard players set START_TIME START_TIME 0

scoreboard objectives add elapsed_time dummy "elapsed_time"
scoreboard players operation @p elapsed_time = WAIT_TICKS WAIT_TICKS

scoreboard objectives add item_damage dummy "item_damage"

scoreboard objectives setdisplay sidebar elapsed_time
scoreboard objectives setdisplay sidebar item_damage
